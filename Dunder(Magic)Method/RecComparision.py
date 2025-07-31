class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

r1 = Rectangle(5, 10)
r2 = Rectangle(7, 8)
print(r1 > r2)
print(r1 < r2)
print(r1 == r2) 
