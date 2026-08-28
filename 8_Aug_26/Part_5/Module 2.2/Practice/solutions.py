# ============================================================
# Module 2.2 - Practice Solutions (Reference)
# Folder: Module 2.2/Practice/solutions.py
# Do not open until you try questions.py first!
# ============================================================

print("--- Q1 ---")
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(1, 11, 2)))

print("\n--- Q2 ---")
for item in ["Apple", "Banana", "Mango"]:
    print(item)

print("\n--- Q3 ---")
platform = "Ostad"
for char in platform:
    print(char)

print("\n--- Q4 ---")
fruit_list = ["Apple", "Banana", "Cherry", "Orange", "Mango", "Pineapple"]
print(fruit_list[3])
print(fruit_list[-1])

print("\n--- Q5 ---")
items = ["Apple", "Banana", "Mango", "Guava"]
for item in items:
    print(f"Fahim, {item}, {len(item)}")

print("\n--- Q6 ---")
for i in range(1, 10, 2):
    print(i)
for i in range(1, 10):
    print(i * 3)

print("\n--- Q7 ---")
fruit_list = ["Apple", "Banana", "Cherry", "Orange", "Mango", "Pineapple"]
fruit_list.append('pie')
print(fruit_list)
fruit_list.insert(2, "mana")
print(fruit_list)
fruit_list.pop(2)
print(fruit_list)

print("\n--- Q8 ---")
ran = [1, "Eea", 3.45, True]
for x in ran:
    print(f"{x} -> {type(x)}")

print("\n--- Q9 & Q10 ---")
number = [1, 4, 3, 6, 10]
sq_num = [i ** 2 for i in number]
print(sq_num)
even_num = [i for i in number if i % 2 == 0]
print(even_num)

print("\n--- Q11 ---")
upper_item = ["shirt", "panjabi", "fatua"]
lower_item = ["jeans", "payjama", "trouser"]
for i in upper_item:
    for j in lower_item:
        print(f"{i}-{j}")

print("\n--- Q12 ---")
platform = "Ostad"
count = 0
for char in platform:
    count += 1
print(f"Total characters: {count}")

print("\n--- Q13 ---")
word_list = ["shirt", "panjabi", "fatua", "jeans", "payjama"]
long_words = [w for w in word_list if len(w) > 5]
print(long_words)

print("\n--- Q14 ---")
nums = [1,2,3,4,5,6,7,8,9,10]
sq_even = [i**2 for i in nums if i % 2 == 0]
print(sq_even)

print("\n--- Q15 ---")
sentence = "Programming in Python is Fun"
vowels = "aeiouAEIOU"
count = 0
found = []
for char in sentence:
    if char in vowels:
        count += 1
        found.append(char)
print(f"Total vowels: {count}")
print(found)
# comprehension version
found2 = [c for c in sentence if c in vowels]
print(found2)

print("\n--- Q16 ---")
n = 5
# A) nested loops
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
# B) comprehension
stars = ["*" * i for i in range(1, n+1)]
for s in stars:
    print(s)
