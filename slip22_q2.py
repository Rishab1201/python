list = []

n = int(input('Enter a number :: '))

for i in range(n):
    num = int(input('Enter numbers : '))
    list.append(num)

print(list)

for i in range(n):
    for j in range(n - i - 1):
        if list[j] > list[j+1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print(list)