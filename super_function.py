
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"{self.color} and is {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius


    def describe(self):
        print(f'It is a circle with area of {3.14 * self.radius * self.radius} and color {self.color}')
        super().describe() #this one actually specifically calls only the parent method of describe

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


    def describe(self):
        print(f'It is a square of area {self.width * self.width} and color {self.color}')
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


    def describe(self):
        print(f'It is a triangle of area {(1/2) * self.width * self.height} and color {self.color}')
        super().describe()

circle = Circle(color = 'red', is_filled = True, radius = 2)
square = Square(color = 'blue', is_filled = False, width = 2)
triangle = Triangle(color = 'green', is_filled = True, width = 2, height = 2)

print(circle.color)
print(circle.is_filled)
print(circle.radius)

print(square.color)
print(square.is_filled)
print(square.width)

print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)

circle.describe()
square.describe()
triangle.describe()

#if same methods exist in the parent and the child class,
#then the method of the child class will get called and not the parent