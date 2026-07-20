a = [1,2,3,"Fahim",9.8, True]

print(a)
a[0] = 10
print(a)

s = "Hello"
print(list(s))

a.append([1,2,3,])
print(a)

t = (1,2,3,"Fahim",9.8, True)
t_r = tuple(reversed(t))
print(t)
print(t_r)