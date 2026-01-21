def get_nr_item(user_input):
    item = user_input.split(',')
    return len(item)

user_input = input("Enter items separated by commas: ")
number_of_items = get_nr_item(user_input)

print(f"you have entered {number_of_items} items")