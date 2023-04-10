class shape:
    def area(self):
        pass
    def volume(self):
        pass

class Square(shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
    def volume(self):
        return self.length ** 3

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
    def volume(self):
        return (4/3) * 3.14 * (self.radius ** 3)

l = int(input('Enter Length of square : '))
square = Square(l)

r = int(input('Enter Radius of circle : '))
circle = Circle(r)

print(f'Area Of Square : {square.area()}\nVolume Of Square: {square.volume()}\n')
print(f'Area Of Circle : {circle.area()}\nVolume Of Circle : {circle.volume()}\n')