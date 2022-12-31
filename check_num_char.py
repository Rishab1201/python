#WAP to find wheather given input is number or character.

n = input("Enter something:")

if n.isdigit():
    print("Is a number.")

elif n.isalpha():
    print("Is character.")

else:
    print("Special character.")