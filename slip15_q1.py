# Write a Python class named Student with two attributes student name, marks. Modify the
# attribute values of the said class and print the original and modified values of the said
# attributes.


class student :

    def __init__(self,n,m):
        self.name = n
        self.marks = m

        #original values
        print('Origanl value :- ')
        print('Name of value :- ',self.name)
        print('Marks of student :- ',self.marks)

    def modify(self):
        print('Enter modified values')
        self.name = input('Enter name to be modified :- ')
        self.marks = input('Enter marks to be modified :- ')

        print('Modified values ')
        print('Modified Name :- ',self.name)
        print('MOdified marks :- ',self.marks)

name = input('Enter name of student :- ')
marks = int(input('Enter marks of student :- '))

s1 = student(name,marks)
s1.modify()