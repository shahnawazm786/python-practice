class Car:
    
    def __init__(self,name,milage):
        self.name=name
        self.milage=milage
    
    def __str__(self):
        return f"📌 name of car => {self.name} and giving milage is {self.milage} 📌"
    
    def __add__(self, object2):
        return self.milage + object2.milage
    
c=Car('THAR',20)
print(c)
d=Car('limorgini',120)
print(c+d)