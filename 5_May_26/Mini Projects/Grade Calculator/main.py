# Store multiple subject score
scores = [85, 92, 78, 64, 99]
# print(scores)

# Display the grades
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Score: {score} → Grade: {grade}")

average = sum(scores) / len(scores)

# Calculate the average score and grade
if average >= 90:
    final_grade = "A"
elif average >= 80:
    final_grade = "B"
elif average >= 70:
    final_grade = "C"
elif average >= 60:
    final_grade = "D"
else:
    final_grade = "F"

print(f"Average Score: {average:.2f} → Final Grade: {final_grade}")
