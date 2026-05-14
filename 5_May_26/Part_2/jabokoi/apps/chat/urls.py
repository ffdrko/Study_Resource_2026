from django.urls import path
from .views import (
    ConversationListCreateView, ConversationDetailView, 
    ChatSendMessageView, TripPlanListView, TripPlanDetailView
)

urlpatterns = [
    path('conversations/', ConversationListCreateView.as_view(), name='conversation_list'),
    path('conversations/<uuid:pk>/', ConversationDetailView.as_view(), name='conversation_detail'),
    path('send/', ChatSendMessageView.as_view(), name='chat_send'),
    path('plans/', TripPlanListView.as_view(), name='plan_list'),
    path('plans/<uuid:pk>/', TripPlanDetailView.as_view(), name='plan_detail'),
]
