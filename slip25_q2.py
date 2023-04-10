class Basic_operation:
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def display(self):
        print(f'A = {self.a}\nB = {self.b}')

    def add(self):
        c = self.a + self.b
        print(f'Addition of two numbers : {c}')

    def mul(self):
        c = self.a * self.b
        print(f'Multiplication of two numbers :: {c}')

    def sub(self):
        c = self.a - self.b
        print(f"Subtraction Of two numbers :: {c}")

    def divide(self):
        c = self.a / self.b
        print(f'Division Of two numbers :: {c}')

    def mod(self):
        c = self.a % self.b
        print(f'Mod Of number :: {c}')

a = int(input('Enter a number :: '))
b = int(input('Enter a numbre :: '))
obj = Basic_operation(a, b)
obj.add()
obj.mul()
obj.sub()
obj.divide()
obj.mod()