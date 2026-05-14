import datetime

class WeatherService:
    @staticmethod
    def get_mock_weather(city_id, month=None):
        if month is None:
            month = datetime.datetime.now().month

        # Mock weather logic for Bangladesh
        if 6 <= month <= 9: # Monsoon
            return {
                "condition": "Rainy",
                "temp_c": 28,
                "description": "Heavy rainfall expected. Risk of flash floods in hill tracts.",
                "is_risky": True
            }
        elif 11 <= month <= 2: # Winter
            return {
                "condition": "Sunny/Cool",
                "temp_c": 22,
                "description": "Perfect weather for traveling.",
                "is_risky": False
            }
        else:
            return {
                "condition": "Hot",
                "temp_c": 34,
                "description": "Warm and humid.",
                "is_risky": False
            }
