def generator(n):

    a=0
    b=1

    for i in range(0,n):
        c = a+b
        print(a)
        a=b
        b=c

n = int(input("Enter number : "))

if n == 0:
    print(0)

else:
    generator(n)