s = {"apple", "banana", "mango"}
l = ["apple", "banana", "mango"]
t = ("apple", "banana", "mango")


print(s)
print(l)
print(t)

s.discard("cherry")
# s.remove("cherry")
s.add("cherry")

print(s)