class Rectangle:
    def __init__(self, len, width):
        self.len = len
        self.width = width

    def area(self):
        area = self.len * self.width

        print(f"Area of Rectangle : {area}")

    def perimeter(self):
        peri = 2 * (self.len + self.width)

        print(f'Perimeter of Rectangle : {peri}')


l = int(input('Enter Length of Rectangle : '))
w = int(input('Enter Width of Rectangle : '))

obj = Rectangle(l, w)

obj.area()
obj.perimeter()
