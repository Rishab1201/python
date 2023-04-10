original_tuple = (('333', '33'), ('1416', '55'))
new_tuple = ()

for i in original_tuple:
    new_tuple += (tuple(int(j) for j in i),)

print(new_tuple)