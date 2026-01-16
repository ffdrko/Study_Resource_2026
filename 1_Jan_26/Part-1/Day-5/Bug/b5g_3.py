# Bug-Fixing Exercise 3
# Here is another piece of code that contains a bug:

# menu = ["pasta", "pizza", "salad"]

# for i, j in enumerate(menu):
#     print("f{i}.{j}")
# The expected output is this:

# 0.pasta
# 1.pizza
# 2.salad

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")