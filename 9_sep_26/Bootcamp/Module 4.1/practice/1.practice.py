"""
Write a function `check_pass(marks_list)` that checks if a student passed all subjects.

**Example Input 1:**

```python
marks_list = [50, 60, 45, 30]
```

**Example Output 1:**

```python
"Fail"
```
"""
def check_pass(marks_list):
    # Check if every mark is >= 40
    if all(mark >= 40 for mark in marks_list):
        return "Pass"
    else:
        return "Fail"


# Example usage
print(check_pass([50, 60, 45, 30]))  # Output: "Fail"
print(check_pass([50, 60, 45, 40]))  # Output: "Pass"
