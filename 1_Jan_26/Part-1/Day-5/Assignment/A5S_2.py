# In the coding area, we have a list of strings. Add some code that:

# (1) iterates over the list items,

# (2) prints out the index of each item, a colon ":", and the item.

products = ['table', 'chair', 'door']

for index, item in enumerate(products):
    print(index, ':', item)