from rest_framework import serializers
from .models import Conversation, TripPlan


class ChatMessageSerializer(serializers.Serializer):
    conversation_id = serializers.UUIDField(required=False)
    message = serializers.CharField()
    destination_name = serializers.CharField(required=False, allow_blank=True)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    party_size = serializers.IntegerField(required=False, min_value=1)
    total_budget = serializers.IntegerField(required=False, min_value=0)
    hotel_budget = serializers.IntegerField(required=False, min_value=0)
    food_budget = serializers.IntegerField(required=False, min_value=0)

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        if start_date and end_date and end_date < start_date:
            raise serializers.ValidationError("End date must be on or after start date.")
        return attrs

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

class TripPlanSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.name_en', read_only=True)

    class Meta:
        model = TripPlan
        fields = '__all__'
        read_only_fields = ('id', 'conversation', 'user', 'created_at', 'updated_at', 'destination_name')
