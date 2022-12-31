num = int(input("how much elements do you want to enter in array:"))

list = []

list1 = []

for i in range (0,num):
    ele = int(input("Enter number:"))

    list.append(ele)

n = int(input("Enter numbers to slice:"))

list1 = list[0:n]

del list[0:n]

for i in list1:
    list.append(i)

print(list)