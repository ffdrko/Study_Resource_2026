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
        activities = Activity.objects.filter(destination=destination)[:5]
        
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
                "price": hotels[0].price_per_night_bdt if hotels else 2000
            }
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
