n = input('Enter string:')
def count(n):
    upper = 0
    lower = 0
    for i in n:
        if i.islower():
            lower = lower + 1
        elif i.isupper():
            upper = upper + 1
    print("Count of uppercase:",upper)
    print("Coutn of lowercase:",lower)


count(n)