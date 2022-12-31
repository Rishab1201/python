# write a pyhton program to add an item in a tuple.

num = int(input("How many values you want to enter in tuple:"));

list = [];

for i in range (0,num):
    val = input("Enter values:");
    list.append(val);

print(list);

val1 = input("Enter value to add:");

list.append(val1);

tuple1 = tuple(list);
print(tuple1);
