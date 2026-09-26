#write a python program To implement Hierarchical inheritance
class Shape:
    def description(self):
        print("I am a shape.")
class Circle(Shape):
    def area(self, radius):
        print(f"Area of Circle = {3.14 * radius * radius}")
class Rectangle(Shape):
    def area(self, length, breadth):
        print(f"Area of Rectangle = {length * breadth}")
c = Circle()
r = Rectangle()
c.description()
c.area(5)
r.description()
r.area(3, 6)
