class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = self.radius ** 2
        print(f'Area Of Circle :: {a}')

    def circumference(self):
        c = 2 * (3.14) * self.radius
        print(f'Circumference Of Circle :: {c}')


r = int(input('Enter Radius Of Circle :: '))

obj = circle(r)
obj.area()
obj.circumference()
