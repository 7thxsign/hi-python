

class Rectangle:
    def __init__(self, width, height):
        self._width = width # _ resembles a protected member
        self._height = height

    @property
    def width(self):
        return f'{self._width:.2f}cm'

    @property
    def height(self):
        return f'{self._height:.2f}cm'

    @width.setter
    def width(self, new_width):
        if new_width >= self._width:
            self._width = new_width
        else:
            print(f'Width must be greater than 0 or {self._width:.2f}cm')

    @height.setter
    def height(self, new_height):
        if new_height >= self._height:
            self._height = new_height
        else:
            print(f'Height must be greater than 0 or {self._height:.2f}cm')

    @width.deleter
    def width(self):
        del self._width
        print('Width deleted.')

    @height.deleter
    def height(self):
        del self._height
        print('Height deleted.')


rectangle = Rectangle(10, 20)
print(rectangle.width)
print(rectangle.height)

print(rectangle._width) #protected member access warning
print(rectangle._height) #protected member access warning

rectangle.width = 25
rectangle.height = 45

print(rectangle.width)
print(rectangle.height)

rectangle.width = 20
rectangle.height = 40

del rectangle.width
del rectangle.height
