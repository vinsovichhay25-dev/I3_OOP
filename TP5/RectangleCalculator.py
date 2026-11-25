class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        if not Rectangle.is_valid(self.width, self.length):
            return "Invalid dimensions"
        else:
            return self.width * self.length

    def perimeter(self):
        if not Rectangle.is_valid(self.width, self.length):
            return "Invalid dimensions"
        else:
            return 2 * (self.width + self.length)

    @staticmethod
    def is_valid(width, length):
        if width <= 0 or length <= 0 and  width == length:
            return False
        return True


rec1 = Rectangle(5, 10)
rec2 = Rectangle(-3, 7)  
rec3 = Rectangle(0, 4)  

print("Rectangle 1:", "Area:", rec1.area(), ", Perimeter:", rec1.perimeter())
print("Rectangle 2:", "Area:", rec2.area(), ", Perimeter:", rec2.perimeter())
print("Rectangle 3:", "Area:", rec3.area(), ", Perimeter:", rec3.perimeter())
