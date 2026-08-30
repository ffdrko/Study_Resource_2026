t = (1, 2, 3, 4, 5, 1, 2)

print(type(t))
print(t)
print(t[1])

# unpack tuple

t = (1, 3, "Hello", "World")

a, b, c, d = t

print(a)
print(b)
print(c)
print(d)

t = (1, 3, "Hello", "World")

*a, b, c = t

print(a)
print(b)
print(c)

t = (1, 3, "Hello", "World")

a, *b, c = t

print(a)
print(b)
print(c)

t = (1, 3, "Hello", "World")

a, *b = t

print(a)
print(b)
print(c)

print(t.count(3))
print(t.index(1))