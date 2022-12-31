num = int(input("how much elements do you want to enter in array:"))

list = []

for i in range (0,num):
    ele = int(input("Enter number:"))

    list.append(ele)


m = max(list)

print("maximum value is array:",m)
