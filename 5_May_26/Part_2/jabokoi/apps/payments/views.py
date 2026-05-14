import uuid
from rest_framework import generics, permissions
from .models import Payment
from .serializers import PaymentSerializer


class PaymentListCreateView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Payment.objects.filter(booking__user=self.request.user).select_related('booking')

    def perform_create(self, serializer):
        serializer.save(
            status='completed',
            transaction_id=f"TXN-{uuid.uuid4().hex[:12].upper()}",
        )
