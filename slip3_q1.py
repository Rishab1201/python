dis = {}

n = int(input('how many values you want to enter:'))

for i in range(n):
    newkey1 = input('Enter key:')
    newvalue1 = input('Enter value:')
    dis[newkey1] = newvalue1

print(dis)


checkkey = input('Enter key to check:')
if checkkey in dis:
    dis.pop(checkkey)
    newkey = input('Enter new key:')
    newvalue = input('Enter new value:')
    dis[newkey] = newvalue
    print(dis)
else:
    print('key does not exists')
