# Practice Problems: Variables & Arithmetic
# Solve each problem below.

# 1. Create variables x = 15 and y = 4.
#    Print their sum, difference, product, and division (all four).

x= 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)


# 2. Create a variable to store your age and another for your friend's age.
#    Print who is older by printing the difference.

my_age = 30
frd_age = 28

print(my_age - frd_age)

# 3. The price of one pen is 8 taka. You buy 12 pens.
#    Use variables to calculate and print the total cost.

pen_price = 8
user_quantity = 12

total_cost = pen_price * user_quantity

print(f"The total cost {total_cost}")

# 4. Swap two variables:
#    a = 5, b = 10 -> make a = 10 and b = 5, then print both.

a = 5
b = 10

c = a

a = b
b = c

print(a)
print(b)

# 5. A rectangle has length 7 and width 3.
#    Store them in variables and print the area and perimeter.

length = 7
width = 3

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area} and Perimeter: {perimeter}")