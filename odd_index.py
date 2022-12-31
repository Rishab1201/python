# write a python to remove the characters which have odd index value of given string.

string = input("Enter a string:")

str = ""

for i in range (len(string)):
    if i % 2 == 0:
        str = str + string[i]

print(str)