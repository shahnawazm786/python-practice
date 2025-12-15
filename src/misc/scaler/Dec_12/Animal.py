class Animal:
    def __init__(self,name,color,speak):
        self.name=name
        self.color=color
        self.speak=speak

    def speaks(self):
        print(f'{self.name} speaks {self.speak}')
    
    def __str__(self):
        return f'{self.name} is {self.speak}'
    
            
