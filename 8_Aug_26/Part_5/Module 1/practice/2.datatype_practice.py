# Practice Problems: Data Types & Type Conversion
# Solve each problem below.

# 1. Print the type of these values: 10, 3.14, "hello", True
print(type(10))
print(type(3.14))
print(type("hello"))
print(type(True))

# 2. Convert the string "45" to an integer and add 5 to it. Print the result.

num_str = "45"

str_num = int(num_str) + 5

print(str_num)
# 3. Convert the number 100 to a string and concatenate it with " points".

num = 100
str_num = str(num)

print(str_num + " " + "points")
# 4. Take the float 9.99 and convert it to an integer. Print what you get.
#    What happened to the decimal part?

float_num = 9.99
int_num = int(float_num)

print(int_num) # here we are getting 9 as in case of integer they don't count any decimal points, they consider them as whole number

# 5. Predict first, then run:
#    print(type(10 / 2))   -> int or float? -> float, normal division consider the decimal points
#    print(type(10 // 2))  -> int or float? -> int, floor division only consider the whole number
