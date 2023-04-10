
class str:

    def get_string(self):
        self.char = input('Enter string:')

    def print_string(self):
        print(self.char)
        char1 = self.char.upper()
        print('Entered string in uppercase :- ',char1)

d1 = str()

d1.get_string()
d1.print_string()

