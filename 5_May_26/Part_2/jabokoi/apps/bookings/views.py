import uuid
from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).select_related('trip_plan')

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            status='confirmed',
            provider_ref=f"MOCK-{uuid.uuid4().hex[:10].upper()}",
        )
