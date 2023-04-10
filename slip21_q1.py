class rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area_perimeter(self):
        a = self.width * self.length
        print(f'Area Of Rectangle :: {a}')
        p = 2 * (self.length + self.width)
        print(f'Perimeter Of Rectangel :: {p}')


w = int(input('Enter Width Of Rectangle :: '))
l = int(input('Enter Length Of Rectangle :: '))

obj = rectangle(w, l)
obj.area_perimeter()
