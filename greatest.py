# WAP to find out greatest of 3 number.

num = int(input("Enter 1st number:"))

num1 = int(input("Enter 2nd number:"))

num2 = int(input("Enter 3rd number:"))

if ((num > num1) and (num > num2)):
    print(num,"is greatest of 3 number.")

elif num1 > num and num1 > num2:
    print(num1,"is greatest of 3 number.")

elif num2 > num and num2 > num1:
    print(num2,"is greatest of 3 number.")

else:
    print("All the 3 numbers are same.")