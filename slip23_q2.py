class circle:
    def __init__(self, radius):
        self.radius = radius

    def display(self):
        self.area = self.radius ** 2
        print(f"Area Of Circle :: {self.area}")

    def __add__(self, other):
        return self.area + other.area

n = int(input('Enter Radius :: '))
obj = circle(n)
obj.display()

num = int(input('Enter Radius :: '))
obj1 = circle(num)
obj1.display()

p3 = obj + obj1

print(f'Adding Area Of Two Circles :: {p3}')