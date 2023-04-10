lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

a, b, c = zip(*lst)

print(list(a))
print(list(b))
print(list(c))