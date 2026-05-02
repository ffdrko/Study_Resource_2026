number = [10, 3, 8, 7, 2, 5, 12]
even_num = []
odd_num = []

for i in number:
    if i % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)


print("=== NUMBER ANALYSIS ===")
print(f"Original list: {number}")
print(f"Even number list: {even_num}")
print(f"Odd number list: {odd_num}")