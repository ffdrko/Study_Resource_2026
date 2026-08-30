old_subscriber = {"rafin@gmail.com", "shafin@gmail.com", "sadia@gmail.com", "hasan@gmail.com"}
new_subscriber = {"sadia@gmail.com", "hasan@gmail.com", "sayem@gmail.com", "adnan@gmail.com"}

print(old_subscriber.union(new_subscriber))
print(old_subscriber.intersection(new_subscriber))
print(new_subscriber.difference(old_subscriber))