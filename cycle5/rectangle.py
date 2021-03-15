class rectangle:
    def __init__(self,length,breadth):
        self.length= length
        self.breadth= breadth
    def area(self):
        print ("area of the rectangle",self.length * self.breadth)
rect=rectangle(10,4)
rect3=rect.area()
rect1=rectangle(6,7)
rect4=rect1.area()
if rect3 <= rect4:
 print("rectangle 1 is greater !!")
elif rect3 > rect4:
 print("rectangle 2 is greater !!")
else:
 print("both are the same !!")


