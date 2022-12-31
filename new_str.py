# WAP to make string from 1st two and last two charaters from given string.

str = input("Enter string:")

str1 = str[0:2]

str2 = ""

i = 0

for i in range (len(str)):
    str2 = str2 + str[i-2]

str3 = str2[0:2]

print(str1+str3)