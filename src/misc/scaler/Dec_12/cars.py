class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Cart:
    
    def __init__(self):
        self.products=[]
    
    def add(self,product):
        self.products.append(product)
    
    def calculate(self):
        return sum(item.price for item in self.products)
    def print(self):
        for item in self.products:
            print(item.name)
            print(item.price)


p1=Item('apple',3000)
p2=Item('apple iphone',40000)
p3=Item('apple desktop',50000)
c=Cart()
c.add(p1)
c.add(p2)
c.add(p3)
c.print()
print(c.calculate())