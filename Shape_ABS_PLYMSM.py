#Create a class named shape and sub classes as Circle, Rectangle and Triangle
#it should define the area and perimeter of the shapes and provides its own implementations
#print the area and perimeter of every shapes available
import math
class Shape:
    def __init__(self,shape):
        self.shape  = shape
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,shape,radius):
        super().__init__(shape)
        self.radius = radius
    def area(self):
        print("The Area of the Circle: ",3.14 * self.radius * self.radius)

    def perimeter(self):
        print("The Perimeter of the Circle: ",2 * 3.14 * self.radius)
class Rectangle(Shape):
    def __init__(self,shape,length,breadth):
        super().__init__(shape)
        self.length = length
        self.breadth = breadth
    def area(self):
        print("The Area of the Rectangle: ",self.length * self.breadth)
    def perimeter(self):
        print("The Perimeter of the Rectangle: ",2 * (self.length + self.breadth))
class Triangle(Shape):
    def __init__(self,shape,side1,side2,side3):
        super().__init__(shape)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def perimeter(self):
        print("The Perimeter of the Triangle: ",self.side1 + self.side2 + self.side3)
    def area(self):
        s=(self.side1 + self.side2 + self.side3)/2
        area = math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
        print("The Area of the Triangle: ",area)
class AreaCalculator:
    def areaCalc(shape):
        return shape.area()
class PerimeterCalculator:
    def perimetercalc(shape):
        return shape.perimeter()
    

C=Circle("Circle",5)
R=Rectangle("Rectangle",5,5)
T=Triangle("Triangle",3,4,5)
C.area()
C.perimeter()
R.area()
R.perimeter()
T.area()
T.perimeter()
