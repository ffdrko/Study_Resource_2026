numbers = [1, 7, 8, 4, 3]

sqaure_number = []
for num in numbers:
    sqaure_number.append(num ** 2)

print(sqaure_number)

comprehension = [x ** 2 for x in numbers]

print(comprehension)

set_num = {1, 7, 8, 4, 3, 1, 7, 8, 4, 3}

uni_set = set()

for num in set_num:
    uni_set.add(num ** 2)

print(uni_set)

comprehension_set = {x ** 2 for x in set_num}

print(comprehension_set)

t_numbers = (1, 7, 8, 4, 3)
t_sq = tuple(x ** 2 for x in t_numbers)
print(t_sq)


price_list = {"Rich": 60, "Salt": 30, "Sugar": 100}

print(price_list)

offer_price = {}

for item, price in price_list.items():
    offer_price[item] = price * 0.9

print(offer_price)

offer = {item : price * 0.9 for item, price in price_list.items()}

print(offer)

filer_offer = {item : price * 0.9 for item, price in price_list.items() if item != "Salt"}

print(filer_offer)