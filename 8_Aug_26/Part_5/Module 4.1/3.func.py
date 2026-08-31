def tax_price(price, tax):
    total_price = price + price * tax
    print(total_price)
    return total_price


tax_price(price= 100, tax= 0.15)
tax_price(tax=0.15, price=100)