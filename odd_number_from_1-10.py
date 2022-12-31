# WAP to odd number from 1-10

num = int(input("Enter the number:"))

add = 0

for i in range (0,num):
    if i % 2 !=0:
        add = add + i

    
print(add)