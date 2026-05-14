from rest_framework import generics, permissions
from .models import Destination, Hotel, Restaurant, Activity, TransportRoute
from .serializers import (
    DestinationSerializer, HotelSerializer, RestaurantSerializer,
    ActivitySerializer, TransportRouteSerializer
)

class DestinationListView(generics.ListAPIView):
    queryset = Destination.objects.filter(is_active=True)
    serializer_class = DestinationSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = ['division', 'type', 'monsoon_risk']

class DestinationDetailView(generics.RetrieveAPIView):
    queryset = Destination.objects.filter(is_active=True)
    serializer_class = DestinationSerializer
    permission_classes = (permissions.AllowAny,)

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.filter(is_active=True)
    serializer_class = HotelSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_fields = ['destination', 'price_tier', 'star_rating']
