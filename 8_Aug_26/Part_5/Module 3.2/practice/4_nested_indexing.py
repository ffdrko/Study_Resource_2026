"""
Problem 4: Deep Nested Data Access

Given the nested structure below:
Write single-line indexing expressions to retrieve and print:
1. The floor level ("Level 4").
2. The item "Charger".
3. The color "Blue".
"""

store_data = [
    "TechZone",
    {"branch_id": 101, "open": True},
    ("Main Street", "Block B", "Level 4"),
    [
        {"category": "Mobile", "items": ["Phone", "Charger", "Case"]},
        {"category": "Audio", "items": [{"name": "Earbuds", "colors": ["Black", "White", "Blue"]}]}
    ]
]

# Write your print statements below:
# 1. Print "Level 4":
print(store_data[2][-1])
# 2. Print "Charger":
print(store_data[3][0]["items"][1])
# 3. Print "Blue":
print(store_data[3][1]["items"][0]["colors"][-1])
