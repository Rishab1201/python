# write a python program to create a tuple with different data types.

num = int(input("How many values do you want to enter:"));

a = tuple()

for i in range (0,num):
    val = input("Enter values:");
    a.add(val);

print(a);