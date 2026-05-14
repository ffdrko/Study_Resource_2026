from rest_framework import generics, permissions, status
from rest_framework.response import Response
from destinations.models import Destination
from .models import Conversation, TripPlan
from .serializers import ChatMessageSerializer, ConversationSerializer, TripPlanSerializer
from .plan_generator import PlanGenerator
from .weather_service import WeatherService


def _resolve_price_tier(total_budget):
    if total_budget < 15000:
        return 'budget'
    if total_budget < 40000:
        return 'midrange'
    return 'premium'

class ConversationListCreateView(generics.ListCreateAPIView):
    serializer_class = ConversationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ConversationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConversationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)

class ChatSendMessageView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChatMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payload = serializer.validated_data

        conversation = self._get_or_create_conversation(payload.get('conversation_id'))
        messages = list(conversation.messages)
        messages.append({"role": "user", "content": payload['message']})

        missing_fields = self._missing_fields(payload)
        if missing_fields:
            assistant_message = (
                "I can build your Bangladesh trip plan once you share: "
                + ", ".join(missing_fields)
                + "."
            )
            messages.append({"role": "assistant", "content": assistant_message})
            conversation.messages = messages
            conversation.save(update_fields=['messages', 'updated_at'])
            return Response(
                {
                    "message": assistant_message,
                    "conversation": ConversationSerializer(conversation).data,
                    "needs_more_details": True,
                },
                status=status.HTTP_200_OK,
            )

        destination = Destination.objects.filter(
            name_en__iexact=payload['destination_name'],
            is_active=True,
        ).first()
        if not destination:
            assistant_message = "I couldn't find that destination yet. Please choose one from the available list."
            messages.append({"role": "assistant", "content": assistant_message})
            conversation.messages = messages
            conversation.save(update_fields=['messages', 'updated_at'])
            return Response(
                {
                    "message": assistant_message,
                    "conversation": ConversationSerializer(conversation).data,
                    "needs_more_details": True,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        budget_data = {
            'party_size': payload['party_size'],
            'total_budget': payload['total_budget'],
            'hotel_budget': payload['hotel_budget'],
            'food_budget': payload['food_budget'],
            'price_tier': _resolve_price_tier(payload['total_budget']),
        }
        weather = WeatherService.get_mock_weather(destination.weather_city_id, payload['start_date'].month)
        plan = PlanGenerator.create_plan_from_ai_response(
            conversation=conversation,
            user=request.user,
            destination_name=destination.name_en,
            start_date=payload['start_date'],
            end_date=payload['end_date'],
            budget_data=budget_data,
        )

        if not plan:
            return Response({"message": "Plan generation failed for that destination."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        risk_note = " Travel carefully during this season." if weather['is_risky'] else ""
        assistant_message = (
            f"Plan ready for {destination.name_en} from {payload['start_date']} to {payload['end_date']}. "
            f"Expected weather: {weather['condition']} at around {weather['temp_c']}°C.{risk_note}"
        )
        messages.append({"role": "assistant", "content": assistant_message})

        conversation.messages = messages
        conversation.status = 'plan_generated'
        conversation.save(update_fields=['messages', 'status', 'updated_at'])

        return Response(
            {
                "message": assistant_message,
                "conversation": ConversationSerializer(conversation).data,
                "plan": TripPlanSerializer(plan).data,
                "weather": weather,
                "needs_more_details": False,
            },
            status=status.HTTP_200_OK,
        )

    def _get_or_create_conversation(self, conversation_id):
        if conversation_id:
            return Conversation.objects.get(id=conversation_id, user=self.request.user)
        return Conversation.objects.create(user=self.request.user, messages=[])

    @staticmethod
    def _missing_fields(payload):
        field_labels = {
            'destination_name': 'destination',
            'start_date': 'start date',
            'end_date': 'end date',
            'party_size': 'party size',
            'total_budget': 'total budget',
            'hotel_budget': 'hotel budget per night',
            'food_budget': 'food budget per day',
        }
        return [label for field, label in field_labels.items() if not payload.get(field)]

class TripPlanListView(generics.ListAPIView):
    serializer_class = TripPlanSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return TripPlan.objects.filter(user=self.request.user)

class TripPlanDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = TripPlanSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return TripPlan.objects.filter(user=self.request.user)
