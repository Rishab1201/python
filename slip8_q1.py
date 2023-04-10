
num = int(input('How many values do you want to enter :- '))

a = []

for i in range(num):
    n = int(input('Enter number:'))
    a.append(n)

# new_array =arr.array('i',a)

my_tuple = tuple(a)

print(my_tuple)

repeated_items = []

for item in set(my_tuple):
    if my_tuple.count(item) > 1:
        repeated_items.append(item)

if len(repeated_items) == 0:
    print("There are no repeated items in the tuple.")
else:
    print("The repeated items in the tuple are:", repeated_items)
