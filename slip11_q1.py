t1 = (1, 2, 3, 4)
t2 = (2, 4, 3, 5)
t3 = (3, 6, 7, 8)

# result = tuple(map(sum,zip(t1,t2,t3)))
# print(result)

result = []

for i in range(len(t1)):
    res = t1[i] + t2[i] + t3[i]
    result.append(res)

print(tuple(result))



