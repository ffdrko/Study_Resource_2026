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

