
n = int(input("Enter the number of elements in the list: "))

my_list = []
for i in range(n):
    num = int(input("Enter a number: "))
    my_list.append(num)


new_list = set(my_list)


print("The list without duplicates is: ", new_list)
