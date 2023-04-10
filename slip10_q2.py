class BracketChecker:
    def __init__(self, input_string):
        self.input_string = input_string

    def is_valid(self):
        stack = []
        for char in self.input_string:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if (opening_bracket == "(" and char != ")") or \
                   (opening_bracket == "[" and char != "]") or \
                   (opening_bracket == "{" and char != "}"):
                    return False
        return not stack


n = input('Enter a string :')

obj = BracketChecker(n)

if obj.is_valid() == True:
    print('String is Valid')
else:
    print('Strng is not valid')