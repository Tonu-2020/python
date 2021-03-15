class Rectangle():
    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    def area(self):
        return self.__length*self.__width

    def __lt__(self):
        if (area1 < area2):
            print("area of rectangle 1 is less than Rectangle 2 !")
        else:
            print("area of rectangle 2 is less than Rectangle 1 !")
rect1=Rectangle(3,4)
rect2=Rectangle(5,6)
area1 = rect1.area()
area2 = rect2.area()
obj=Rectangle(area1,area2)
obj.__lt__()