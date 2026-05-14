# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import Destination, Hotel, Restaurant, Activity, TransportRoute

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'division', 'type', 'monsoon_risk', 'is_active')
    search_fields = ('name_en', 'name_bn', 'division')
    list_filter = ('division', 'type', 'monsoon_risk')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'price_tier', 'star_rating', 'is_active')
    list_filter = ('destination', 'price_tier', 'star_rating')
    search_fields = ('name', 'name_bn')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'price_tier', 'is_active')
    list_filter = ('destination', 'price_tier')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'destination', 'type', 'best_time_of_day')
    list_filter = ('destination', 'type')

@admin.register(TransportRoute)
class TransportRouteAdmin(admin.ModelAdmin):
    list_display = ('origin_city', 'destination_city', 'mode', 'operator', 'avg_cost_bdt')
    list_filter = ('mode', 'origin_city', 'destination_city')
