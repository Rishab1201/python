class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return(f"{self.a} + {self.b}i \n")

    def __add__(self, x):
        return complex(self.a + x.a, self.b + x.b)


obj = complex(2, 4)
print(obj)

obj1 = complex(4, 2)
print(obj1)

print(obj + obj1)