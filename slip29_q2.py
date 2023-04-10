dict = {}

n = int(input('Enter number of key value pair :: '))

for i in range(n):
    key = input('Enter Key :')
    value = input('Enter value :')
    dict[key] = value

print(dict)

sort_ascending = sorted(dict.items(), key=lambda x: x[0])
print(f'Ascending order of key : {sort_ascending}')

sort_descending = sorted(dict.items(), key=lambda x: x[0], reverse=True)

print(f'Descending order of key : {sort_descending}')

sort_dis_value = sorted(dict.items(), key=lambda x: x[1])
print(f'Ascending order of value : {sort_dis_value}')

sort_dis_value_desc = sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(f'Descending order of values : {sort_dis_value_desc}')