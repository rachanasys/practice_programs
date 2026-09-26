#write a python program To implement Operator overloading 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):          # overloads the '+' operator
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):          # overloads the '-' operator
        return Point(self.x - other.x, self.y - other.y)
    def __eq__(self, other):           # overloads the '==' operator
        return self.x == other.x and self.y == other.y
    def __str__(self):                 # used by print()
        return f"Point({self.x}, {self.y})"
p1 = Point(2, 3); p2 = Point(4, 5)
p3 = p1 + p2 ;    p4 = p2 - p1 
print("p1 =", p1);print("p2 =", p2);print("p1 + p2 =", p3);print("p2 - p1 =", p4)
print("p1 == p2 ?", p1 == p2)      # calls __eq__
print("p1 == Point(2,3) ?", p1 == Point(2, 3))
