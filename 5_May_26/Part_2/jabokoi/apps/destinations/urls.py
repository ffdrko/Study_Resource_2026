from django.urls import path
from .views import DestinationListView, DestinationDetailView, HotelListView

urlpatterns = [
    path('', DestinationListView.as_view(), name='destination_list'),
    path('<uuid:pk>/', DestinationDetailView.as_view(), name='destination_detail'),
    path('hotels/', HotelListView.as_view(), name='hotel_list'),
]
