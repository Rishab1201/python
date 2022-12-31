# write a pyhton script to check if a given key already exixts in a dictionary.

num = int(input("how many values you want to enter:"));

dic = {};

for i in range (0,num):
    key = input("Enter key:");
    val = input("Enter values:");

    dic[key] = val;

print(dic);

val1 = input("Enter key to search:");

if val1 in dic:
    print('key is present in dictionary.');

else:
    print('Key is Not present in dictionary.');