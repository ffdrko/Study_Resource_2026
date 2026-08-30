"""
Problem 5: Leaderboard with enumerate()

Given the finishing order of participants in a programming contest:
participants = ["Rahim", "Karim", "Nusrat", "Farhan", "Samiha", "Tanvir"]

Tasks:
1. Use `enumerate()` to iterate over the participants with rank numbers starting at 1.
2. Display a leaderboard with medals for the top 3 and rank numbers for the rest:
   - Rank 1: 1. Rahim (Gold Medal)
   - Rank 2: 2. Karim (Silver Medal)
   - Rank 3: 3. Nusrat (Bronze Medal)
   - Rank 4+: 4. Farhan, 5. Samiha, etc.
"""

participants = ["Rahim", "Karim", "Nusrat", "Farhan", "Samiha", "Tanvir"]

# Write your code below:


for index, name in enumerate(participants, start=1):
    if index == 1:
        print(f"Rank {index}: {index}. {name} (Gold Medal)")
    elif index == 2:
        print(f"Rank {index}: {index}. {name} (Silver Medal)")
    elif index == 3:
        print(f"Rank {index}: {index}. {name} (Bronze Medal)")
    else:
        print(f"Rank {index}: {index}. {name}")
