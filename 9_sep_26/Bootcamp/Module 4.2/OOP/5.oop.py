class ShoppingCart:
    def __init__(self, customer_name, items=None):
        self.customer_name = customer_name
        self.items = items if items is not None else []

   
    def add_item(self, price):
        if price > 0:
            self.items.append(price)
            print(f"Added item priced {price} to {self.customer_name}'s cart.")
        else:
            print("Error: Price must be a positive number.")

    def remove_item(self, price):
        if price in self.items:
            self.items.remove(price)
            print(f"Removed item priced {price} from {self.customer_name}'s cart.")
        else:
            print(f"Item priced {price} not found in {self.customer_name}'s cart.")

    def calculate_total(self):
        return sum(self.items)

    def apply_discount(self):
        total = self.calculate_total()
        if total >= 3000:
            return total * 0.90
        return total

   
    def display_cart(self):
        total = self.calculate_total()
        final = self.apply_discount()
        print("-" * 40)
        print(f"Customer Name : {self.customer_name}")
        print(f"Items in Cart : {self.items}")
        print(f"Total Amount  : {total:.2f}")
        print(f"Final Amount  : {final:.2f} (after discount)")
        print(f"Item Count    : {len(self.items)}")
        print("-" * 40)

    def clear_cart(self):
        self.items = []
        print(f"{self.customer_name}'s cart has been cleared.")

    
    def __add__(self, other):
        combined_name = f"{self.customer_name} & {other.customer_name}"
        combined_items = self.items + other.items
        return ShoppingCart(combined_name, combined_items)



cart1 = ShoppingCart("Alice", [1500, 2200, 500])
cart2 = ShoppingCart("Bob")

cart1.add_item(800)
cart1.remove_item(500)

cart2.add_item(1000)
cart2.add_item(2500)
cart2.remove_item(999)

cart1.display_cart()
cart2.display_cart()

combined_cart = cart1 + cart2
combined_cart.display_cart()

 