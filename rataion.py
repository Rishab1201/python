num = int(input("how much elements do you want to enter in array:"))

list = []

for i in range (0,num):
    ele = int(input("Enter number:"))

    list.append(ele)

print(list)

n = int(input("How many element do you want to rotate:"))

for i in range (0,n):
    del1 = list.pop(0)
    list.append(del1)

print(list)
