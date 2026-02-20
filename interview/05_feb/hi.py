class Shape:


    def __init__(self,cm):
        self.cm = cm
    
    def area(self):
        return self.cm
    

class Square(Shape):
    def __init__(self, cm):
        super().__init__(cm)
        
    
    def area(self):
        return self.cm * self.cm
        



hi = Square(5)

print(hi.area())




#  abstraction :
#  error of the instance has cls attribute what will happpen
#  