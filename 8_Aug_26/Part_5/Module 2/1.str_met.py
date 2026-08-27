course_name = " oStad ai ##booTcamp  "
print(course_name)
course_name = course_name.strip()
print(course_name)
course_name = course_name.lower()
print(course_name)
course_name = course_name.replace("#", "")
print(course_name)
course_name = course_name.title()
print(course_name)

text_book = "  ostAd ##Book"
print(text_book)
# method chaining
text_book = text_book.strip().lower().replace("#","").title()
print(text_book)