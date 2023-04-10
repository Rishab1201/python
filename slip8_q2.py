class String:

    def get_string(self):
        self.str = input('Enter a string : ')

    def print_string(self):
        print("String in Uppercase : ", self.str.upper())

    def reverse(self):
        return self.str[::-1]

s = String()

s.get_string()
s.print_string()
print("Reversed string in lowercase :", s.reverse())
