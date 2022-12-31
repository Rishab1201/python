# python program to find reminder of array multiplication divided by n

num = int(input("how much elements do you want to enter in array:"))

list = []

for i in range (0,num):
    ele = int(input("Enter number:"))

    list.append(ele)

mul = 1
for i in list:
    mul = mul * i

print("Multiplication of array:",mul)

n = int(input("Enter the number:"))

rem = mul % n

print("Reminder of array:%d"%(rem))