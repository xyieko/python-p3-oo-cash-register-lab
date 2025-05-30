class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.total = 0
        self.discount = discount
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
        self.total += price * quantity
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount / 100)
            if self.total.is_integer():
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")
        return self.total

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.items.pop()