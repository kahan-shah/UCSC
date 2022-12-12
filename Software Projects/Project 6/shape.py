# Kahan Shah
# Shape Assignment
# This program creates a basic shape and find the area perimeter and tells what the shape is.

import math
class Shape:
    # shape id contructor
    def __init__(self,Shape_id):
        self.Shape_id=Shape_id
    # string identifier return method
    def get_id(self):
        return self.Shape_id
    # area of the shape return method
    def get_area(self):
        print("Area cannot be calculated")
        return None
    # perimeter (or circumference) return method
    def get_perimeter(self):
        print('perimeter cannot be calculated')
        return None

# Ellipse derived from the Shape class
class Ellipse(Shape):
    # constructor for radius and shape id
    def __init__(self,major_axis_radius,minor_axis_radius,Shape_id):
        self.minor_axis_radius=minor_axis_radius
        self.major_axis_radius=major_axis_radius
        # pass value to super class constructor
        super(Ellipse, self).__init__(Shape_id)
    # return area of an Ellipse
    def get_area(self):
        return math.pi*self.minor_axis_radius*self.major_axis_radius
    def get_perimeter(self):
        print('perimeter cannot be calculated')
        return None   

# Circle derived from Ellipse class
class Circle(Ellipse):
    # constructor which uses Shape_id and radius
    def __init__(self,Shape_id,radius):
        self.radius=radius
        super(Circle, self).__init__(radius,radius,Shape_id)
    # This method returns the area of a circle
    def get_area(self):
        return math.pi*(self.radius**2)
    # This method returns the circumference. 
    def get_perimeter(self):
        return 2*math.pi*self.radius

# Rectangle derived from the Shape class
class Rectangle(Shape):
    # constructor that uses Shape_id,length and width
    def __init__(self,Shape_id,width,length):
        self.width=width
        self.length=length
        # call the parent class's 
        super(Rectangle, self).__init__(Shape_id)
    # This method returns the area of Rectangle    
    def get_area(self):
        return self.length*self.width
    # This method returns the perimeter      
    def get_perimeter(self):
        return 2*(self.length+self.width)
    
# Square derived from the Rectangle class
class Square(Rectangle):
    # The __init__ method takes an identifier and the side length
    def __init__(self,Shape_id,length):
        self.length=length
        super(Square, self).__init__(Shape_id,length,length)
    # This method returns the area of Square 
    def get_area(self):
        return self.length**2
    # This method returns the perimeter.         
    def get_perimeter(self):
        return 4*self.length

# Test code
def main():    
    # create Shape class object
    x = Shape("Shape1A")
    print(x.get_id())
    x.get_area()
    x.get_perimeter()
    # create an object of Ellipse class
    e=Ellipse(6.45,4.45,"Shape2A")
    print(e.get_id())
    print("Area of Ellipse is",e.get_area())
    print("Perimeter of Ellipse is",e.get_perimeter())
    # Create an object of Circle class
    c=Circle("Shape3A",20)
    print(c.get_id())
    print("Area of Circle is",c.get_area())
    print("Perimeter of Circle is",c.get_perimeter())
    # Create an object of Rectangle class
    r=Rectangle("Shape4A",6,4)
    print(r.get_id())
    print("Area of Rectangle is",r.get_area())
    print("Perimeter of Rectangle is",r.get_perimeter())
    # Create an object of Square class
    s=Square("Shape4A",6)
    print(s.get_id())
    print("Area of Square is",s.get_area())
    print("Perimeter of Square is",s.get_perimeter())
    
if __name__ == "__main__":
    main()
