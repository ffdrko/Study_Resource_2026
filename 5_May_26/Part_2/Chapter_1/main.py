# Variable is containers for data

user_name = "Alice"
message_count = 42
reponse_time = 0.357
is_premium_user = True

print(user_name)
print(message_count)
print(reponse_time)
print(is_premium_user)

""" Here in the given program there is no type mention, to find the data type 
we need use type() manually.
to solve these problem we need to use the type hint"""

user_name: str = "Fahim"
age: int = 20
height_m: float = 1.75
coded_before: bool = True 

print(user_name)
print(age)
print(height_m)
print(coded_before)