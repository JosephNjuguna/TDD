class ShoppingCart():

    def __init__(self):#empty constuctor
        self.total = 0 #attributes
        self.items = {} #an attribute with an empty dictionary

    def add_item(self, item_name, quantity, price):
        productprices = price*quantity
        self.total =+ productprices
        if quantity >0 and type (item_name)==str:
            self.items.update({item_name: quantity})

    def remove_item(self, item_name, quantity, price):
        if quantity >= self.items[item_name] and quantity >= 1:
            product_prices = price*self.items[item_name]
            self.total -= product_prices
            del self.items[item_name]
        else:
            self.total -= quantity * price
            self.items[item_name] -= quantity

    def checkout(self,cash_paid):
        balance = 0
        if cash_paid <= self.total:
            return 'cashpaid not enough'
        else:
            balance = cash_paid-self.total
            return balance

class Shop(ShoppingCart):
    def __init__(self):
        quantity = 100
