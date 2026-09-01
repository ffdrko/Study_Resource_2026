# Practice Problems: String Methods
# Solve each problem below. Run the file to check your output.

# 1. Given the string text = " Hello World ", use string methods to:
#    - Remove leading/trailing whitespace
#    - Convert to uppercase
#    - Convert to lowercase
#    - Capitalize the first letter

text = " Hello World "
print(text.strip())
print(text.upper())
print(text.lower())
print(text.strip().capitalize())

# 2. Given the string text = "Python is fun!", use these methods:
#    - count('o')
#    - find('l')
#    - isdigit()
#    - split()

text = "Python is fun!"
print(text.count('o'))
print(text.find('l'))
print(text.isdigit())
print(text.split())


# 3. Given the string text = "Python", use:
#    - index('n')
#    - len(text)

text = "Python"
print(text.index('n'))
print(len(text))


# 4. Given the string greet = " Hello WoRld ", chain methods to:
#    - strip, then lower, then replace '#' (if any), then title()

greet = " Hello WoRld "
print(greet.strip().lower().replace("#","").title())