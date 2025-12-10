'''
Use of donder method 
__init__
__add__
__str__
__lt__
__gt__
'''
class Car:
    
    def __init__(self,name,milage):
        self.name=name
        self.milage=milage
    
    def __str__(self):
        return f"📌 name of car => {self.name} and giving milage is {self.milage} 📌"
    
    def __add__(self, other):
        # if isinstance(other, Car):
        #     return self.milage + other.milage
        # return NotImplemented
        return Car(
                name=f"{self.name}+{other.name}",
                milage=self.milage + other.milage
            )
    
    def __radd__(self,other):
        if other==0:
            return self
        return self.__add__(other)
    
    def __lt__(self,object2):
        return self.milage < object2.milage
    
    def __gt__(self,object2):
        return self.milage > object2.milage

c=Car('THAR',20)
print(c)
d=Car('limorgini',120)
print(c+d)
#print(c<d)
#print(c>d)
e=Car('TATA',200)
print([c,d,e])
#print(result)
print(c+d)
print(d+e)
print(c+d+e)