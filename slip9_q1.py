
class reverse:

    def accept(self):
        self.str = input('Enter a string:')
        l = len(self.str)
        print(l)
        rev = ""

        while l > 0:
            rev = rev + self.str[l-1]
            l = l - 1

        print(rev)

    def setter(self):
        for ch in reversed(self.str):
            print(ch)

obj = reverse()

obj.accept()
obj.setter()