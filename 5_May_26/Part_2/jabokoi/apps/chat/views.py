from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Conversation, TripPlan
from .serializers import ConversationSerializer, TripPlanSerializer

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

    def post(self, request, *args, **kwargs):
        # Placeholder for AI message handling logic
        # Will be implemented in Phase 2 with Claude API integration
        return Response({"message": "Message received (AI logic pending Phase 2)"}, status=status.HTTP_200_OK)

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
