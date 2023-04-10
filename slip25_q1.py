str = input("Enter a string :: ")

upper_cnt = 0
lower_cnt = 0

for i in str:
    if i.islower():
        lower_cnt += 1

    elif i.isupper():
        upper_cnt += 1

print(f'Number Of Upper case Characters :: {upper_cnt}')
print(f'Number Of Lower Case Characters :: {lower_cnt}')