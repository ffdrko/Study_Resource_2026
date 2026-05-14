import random
import uuid

class MockBookingService:
    @staticmethod
    def search_bus_tickets(origin, destination, date):
        # Mock Shohoz search
        operators = ["Hanif Enterprise", "Ena Transport", "Green Line", "Shyamoli Paribahan"]
        results = []
        for op in operators:
            results.append({
                "id": str(uuid.uuid4()),
                "operator": op,
                "departure": "08:30 AM",
                "type": "AC" if random.random() > 0.5 else "Non-AC",
                "price": random.randint(800, 1500)
            })
        return results

    @staticmethod
    def search_flights(origin, destination, date):
        # Mock Biman/US-Bangla
        operators = ["Biman Bangladesh", "US-Bangla Airlines", "Air Astra", "Novoair"]
        results = []
        for op in operators:
            results.append({
                "id": str(uuid.uuid4()),
                "operator": op,
                "departure": "10:00 AM",
                "price": random.randint(4500, 8500)
            })
        return results

    @staticmethod
    def book_item(item_id, user_email):
        # Mock booking action
        return {
            "status": "success",
            "confirmation_code": f"JK-{random.randint(100000, 999999)}",
            "message": f"Successfully booked for {user_email}"
        }
