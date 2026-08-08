"""
2. 📞 Extract Country Code from Phone Number
"""

user_number = input("Enter your phone number (with country code): ")

country_code = user_number[:4]  # Extract the country code
print("Country code:", country_code)