'''
You are designing a small part of an e-commerce system. A user should be able to: Add products to a cart
Store product name & price
Calculate the final total
'''
class Product:
    
    def __init__(self,name,price):
        self.product={}
    def add_product(self,name,price):
        if name in self.product:
        # product exists → add price
            self.product[name] += price
        else:
        # product does not exist → create new
            self.product[name] = price

    def calculate(self):
        return  sum(self.product.values())
