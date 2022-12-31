# write a python script to merge two python dictionaries.

num = int(input("how many values you want to enter:"));

dic = {};
dic1 = {};

for i in range(0,num):
    key = input("Enter a key:");
    val = input("Enter values:");
    dic[key] = val;

print(dic);

num1 = int(input("how many values you want to enter in 2nd dictionary:"));

for i in range (0,num1):
    key1 = input("Enter a key:");
    val1 = input("Enter values:");
    dic1[key1] = val1;

print(dic1);

print("------------AFTER MERGING TWO DICTIONARIES----------------");

dic2 = {};

dic2 = dic | dic1;

print(dic2);



