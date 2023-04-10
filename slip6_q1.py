
from MyModules import functions

num = int(input('Enter side of cube :- '))

area = functions.area_Of_cube(num)

print('Area of cube :- ',area)

volume = functions.volume_Of_cube(num)

print('Volume of cube :- ',volume)

n =  int(input('Enter radius :- '))

ar = functions.area_Of_sphere(n)

print('Area of sphere :- ',ar)

vol = functions.volume_Of_sphere(n)

print('Volume of sphere :- ',vol)