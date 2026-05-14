import json
from .models import TripPlan
from destinations.models import Destination, Hotel, Activity, TransportRoute

class PlanGenerator:
    @staticmethod
    def create_plan_from_ai_response(conversation, user, destination_name, start_date, end_date, budget_data):
        # In a real scenario, we would parse the AI response to get these details.
        # For the prototype, we'll fetch real items from our DB based on the destination.
        
        try:
            destination = Destination.objects.get(name_en__iexact=destination_name)
        except Destination.DoesNotExist:
            return None

        # Fetch some items for the plan
        hotels = Hotel.objects.filter(destination=destination, price_tier=budget_data.get('price_tier', 'midrange'))[:1]
        if not hotels:
            hotels = Hotel.objects.filter(destination=destination).order_by('price_per_night_bdt')[:1]
        activities = Activity.objects.filter(destination=destination)[:5]
        transport = TransportRoute.objects.filter(
            destination_city__iexact=destination.name_en,
            is_active=True,
        ).order_by('avg_cost_bdt')[:2]
        
        # Build mock itinerary
        itinerary = []
        days = (end_date - start_date).days + 1
        for i in range(days):
            itinerary.append({
                "day": i + 1,
                "activities": [
                    {"time": "Morning", "activity": activities[i % len(activities)].name_en if activities else "Sightseeing"},
                    {"time": "Afternoon", "activity": "Local Exploration"},
                    {"time": "Evening", "activity": "Dinner at a local restaurant"}
                ]
            })

        plan_data = {
            "itinerary": itinerary,
            "hotel": {
                "name": hotels[0].name if hotels else "Standard Hotel",
                "price": hotels[0].price_per_night_bdt if hotels else 2000,
                "booking_url": hotels[0].booking_url if hotels else None,
            },
            "transport": [
                {
                    "mode": route.mode,
                    "operator": route.operator,
                    "avg_cost_bdt": route.avg_cost_bdt,
                    "avg_duration_minutes": route.avg_duration_minutes,
                    "booking_url": route.booking_url,
                }
                for route in transport
            ],
            "budget_breakdown": {
                "hotel_total": (hotels[0].price_per_night_bdt if hotels else 2000) * days,
                "food_total": budget_data.get('food_budget', 1000) * days,
                "transport_total": sum(route.avg_cost_bdt for route in transport) or max(1000, days * 500),
            },
        }

        plan = TripPlan.objects.create(
            conversation=conversation,
            user=user,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            party_size=budget_data.get('party_size', 1),
            total_budget_bdt=budget_data.get('total_budget', 20000),
            hotel_budget_per_night_bdt=budget_data.get('hotel_budget', 3000),
            food_budget_per_day_bdt=budget_data.get('food_budget', 1000),
            plan_data=plan_data
        )
        return plan
