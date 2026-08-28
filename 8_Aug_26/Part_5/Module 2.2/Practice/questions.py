# ============================================================
# Module 2.2 - Practice Question Set
# Folder: Module 2.2/Practice/
# File: questions.py
# Topics Covered:
#   - for loop & range()          -> 0_for.py, 1_for_1.py
#   - string iteration            -> 2.for.py:3
#   - nested for loops            -> 2.for.py:10
#   - list indexing/append/insert/pop -> 3.list.py
#   - list comprehension          -> 4_compre.py
# ============================================================
# INSTRUCTION: Solve each problem below the TODO line.
# Do not change the given variables.

# ------------------------------------------------------------
# LEVEL 1: EASY (Warm-up)
# ------------------------------------------------------------

# Q1. range() Basics
# Print list(range(5)), list(range(1,5)), list(range(1,11,2))
# Expected in console: [0,1,2,3,4] etc.
# TODO:
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(1, 11, 2)))

# Q2. Loop Over List
# fruits = ["Apple", "Banana", "Mango"]
# Print each fruit on a new line using for loop.
# TODO:
fruits_q2 = ["Apple", "Banana", "Mango"]

for i in fruits_q2:
    print(i)

# Q3. String Loop
# platform = "Ostad"
# Print each character vertically.
# TODO:
platform = "Ostad"

for i in platform:
    print(i)
# Q4. List Indexing
# fruit_list = ["Apple", "Banana", "Cherry", "Orange", "Mango", "Pineapple"]
# a) Print index 3, b) Print last element with -1
# TODO:
fruit_list = ["Apple", "Banana", "Cherry", "Orange", "Mango", "Pineapple"]

print(fruit_list[2])
print(fruit_list[-1])

# ------------------------------------------------------------
# LEVEL 2: MEDIUM (Core Concepts)
# ------------------------------------------------------------

# Q5. f-string + len()
# Given: items = ["Apple", "Banana", "Mango", "Guava"]
# Print: "Fahim, Apple, 5" for each item.
# Refer: 1_for_1.py:4
# TODO:
items = ["Apple", "Banana", "Mango", "Guava"]

for i in items:
    print(f"Fahim, {i}, {len(i)}")

# Q6. range() with step & math
# a) Print odd numbers 1 to 9 using range(1,10,2)
# b) Print multiples of 3 (i*3) for i in range(1,10)
# Refer: 1_for_1.py:9-13
# TODO:

print(list(range(1, 10, 2)))
print([i * 3 for i in range(1, 10)])


# Q7. List Operations - Append/Insert/Pop
# Start with fruit_list from Q4
# a) Append 'pie' , b) Insert 'mana' at index 2, c) Pop index 2
# Print list after each step.
# Refer: 3.list.py:9-15
# TODO:

fruit_list.append('pie')
print(fruit_list)
fruit_list.insert(2, 'mana')
print(fruit_list)
fruit_list.pop(2)
print(fruit_list)


# Q8. Mixed List
# ran = [1, "Eea", 3.45, True]
# Loop and print each element with its type -> e.g. "1 is int"
# TODO:
ran = [1, "Eea", 3.45, True]

for i in ran:
    print(f"{i} is {type(i)}")

# Q9. List Comprehension - Square
# number = [1, 4, 3, 6, 10]
# Create sq_num = [i**2 for i in number] and print it.
# Expected: [1, 16, 9, 36, 100]
# Refer: 4_compre.py:3
# TODO:
number = [1, 4, 3, 6, 10]

sq_num = [i**2 for i in number]
print(sq_num)


# Q10. List Comprehension - Filter Even
# From same number list, create even_num with even numbers only.
# Expected: [4, 6, 10]
# Refer: 4_compre.py:7
# TODO:

even_num = [i for i in number if i %2 == 0]
print(even_num)
# ------------------------------------------------------------
# LEVEL 3: HARD (Logic Building)
# ------------------------------------------------------------

# Q11. Nested Loop - Combination
# upper_item = ["shirt", "panjabi", "fatua"]
# lower_item = ["jeans", "payjama", "trouser"]
# Print all 9 combos as "shirt-jeans" ... use nested for loops.
# Refer: 2.for.py:10-12
# TODO:
upper_item = ["shirt", "panjabi", "fatua"]
lower_item = ["jeans", "payjama", "trouser"]


for i in upper_item:
    for j in lower_item:
        print(f"{i}-{j}")

# Q12. Loop Counter Without len()
# For platform = "Ostad", count characters using a counter variable in loop.
# Print: "Total characters: 5"
# TODO:

count = 0

for i in platform:
    count = count + 1

print(f"Total characters: {count}")

# Q13. Comprehension with Condition - Length Filter
# word_list = ["shirt", "panjabi", "fatua", "jeans", "payjama"]
# Create new list with words where len > 5
# Expected: ['panjabi', 'payjama']
# TODO:
word_list = ["shirt", "panjabi", "fatua", "jeans", "payjama"]

for i in word_list:
    if len(i) > 5:
        print(i)

# Q14. One-Line Master
# nums = [1,2,3,4,5,6,7,8,9,10]
# In ONE comprehension, create squares of even numbers only.
# Expected: [4, 16, 36, 64, 100]
# TODO:
nums = [1,2,3,4,5,6,7,8,9,10]

even = [ i ** 2 for i in nums if i % 2 == 0]
print(even)

# ------------------------------------------------------------
# LEVEL 4: CHALLENGE (Exam Style - 2 Problems)
# ------------------------------------------------------------

# Q15. [CHALLENGE 1] Vowel Counter with Loop
# sentence = "Programming in Python is Fun"
# Count vowels (a,e,i,o,u both upper/lower) using for char in sentence
# and print total count. Bonus: Create list of found vowels using comprehension.
# TODO:
sentence = "Programming in Python is Fun"

vowels= ['a','e', 'i','o','u']
count =0

for char in sentence.lower():
    if char in vowels:
        count = count + 1

print(f"Total vowels inside the sentence is {count}")
# Q16. [CHALLENGE 2] Star Pattern - Two Ways
# n = 5
# A) Use nested loops to print:
# *
# **
# ***
# ****
# *****
# B) Then do same in ONE line using comprehension: stars = ["*"*i for i in range(1,n+1)]
# and loop to print it.
# TODO:
n = 5

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

stars = ["*"*i for i in range(1,n+1)]

for i in stars:
    print(i)


print("\n=== All Questions Loaded. Start Solving! ===")
