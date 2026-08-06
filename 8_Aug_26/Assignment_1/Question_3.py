user_input = input("Enter temperature in Celsius: ")

# Convert the input to float to handle decimal values
celsius = float(user_input)

# Calculate Fahrenheit using the formula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Print the result
print(f"Temperature in Fahrenheit is: {fahrenheit}°F")