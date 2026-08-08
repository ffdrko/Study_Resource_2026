text = "Python"

print(text[1:4])    # Output: "yth" → from index 1 to 4 (4 excluded)
print(text[:3])     # Output: "Pyt" → from start (0) to index 3 (excluded)
print(text[3:])     # Output: "hon" → from index 3 to end

print(text[::-1])   # Output: "nohtyP" → reverse string
print(text[::2])    # Output: "Pto" → every 2nd character (step = 2)

print(text[-1:-3:-1])      # Output: "n" → last character

print(text[-6:-1:-1])