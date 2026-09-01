"""
Write a function `grade_summary(student_marks_dict)` that returns average marks and highest scoring subject.

**Example Input 1:**

```python
student_marks = {"math": 85, "english": 72, "science": 90}
```

**Example Output 1:**

```python
(82.33, "science")

"""

def grade_summary(student_marks_dict):
    # Extract marks
    marks = list(student_marks_dict.values())
    
    # Calculate average
    average = sum(marks) / len(marks)
    
    # Find subject with highest mark
    highest_subject = max(student_marks_dict, key=student_marks_dict.get)
    
    # Round average to 2 decimal places
    return (round(average, 2), highest_subject)


# Example usage
student_marks = {"math": 85, "english": 72, "science": 90}
print(grade_summary(student_marks))  # Output: (82.33, "science")
