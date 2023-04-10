# Write a python program to accept string and remove the characters which have odd index
# values of given string using user defined function.

def str():

    char = input('Enter string :- ')

    x = list(char)

    str = ''

    for i in range(len(x)):
        if i % 2 != 0:
            x.remove(char[i])

    for i in x :
        str = str + i

    print('Modified String :-',str)

str()