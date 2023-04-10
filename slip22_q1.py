class String:
    def __init__(self, s):
        self.s = s

    def __mul__(self, n):
        return self.s * n

str = input('Enter a String :: ')

obj = String(str)

n = int(input('Enter a number : '))

print(f'{obj.__mul__(n)} \n')

