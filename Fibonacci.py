# Write s python program to get the Fibonacci series between 0 to 50

num = int(input("Enter the range:"))
a=0
b=1

for i in range (0,num):
    c = a+b
    print(a)
    a=b
    b=c
    c=a

    