# We have defined a list of floats in the coding area. Add some code that:

# (1) sorts the list in ascending order,

# (2) iterates over the sorted list

# (3) prints out each item in each iteration

# Here is what the output should look like:

# 166.9

# 175.8

# 177.8

# 182.5

measurements = [177.8, 175.8, 166.9, 182.5]
measurements.sort()

for item in measurements:
    print(item)