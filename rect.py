class Rect:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
obj = Rect(length, breadth)
print("Area of rectangle:", obj.area())
print("Perimeter of rectangle:", obj.perimeter())

