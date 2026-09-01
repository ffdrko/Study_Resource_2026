"""
Write a function `is_item_available(shopping_list, item)` that checks if an item exists.

**Example Input 1:**

```python
shopping_list = ["rice", "oil", "salt"]
item = "oil"
```

**Example Output 1:**

```python
True
```
"""

def is_item_available(shopping_list, item):
    return item in shopping_list


item_found =  is_item_available(["rice", "oil", "salt"], "oil")

print(item_found)