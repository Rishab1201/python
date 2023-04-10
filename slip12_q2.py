# Write a python program to count repeated characters in a string. Sample string:
# 'thequickbrownfoxjumpsoverthelazydog' Expected output: o-4, e-3, u-2, h-2, r-2, t-2

str = input('Enter any string:')

dis = {}

cnt = 0

for i in str:
    cnt = 0
    for j in range(len(str)):
        if i == str[j]:
            cnt = cnt + 1

    if cnt > 1:
        dis[i] = cnt

print(dis)


