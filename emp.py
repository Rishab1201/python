class employee:

    def __init__(self,name,posi,salary):
        self.name = name
        self.posi = posi
        self.salary = salary

    def count(self):
        sala = self.salary * 5 / 100

        self.salary = self.salary + sala

        print('name:',self.name)
        print('position:',self.posi)
        print('salary:',self.salary)


s = int(input("enter salary of employee"))
p = input('Enter position of employee')
n = input("Enter name of employee")

emp = employee(n,p,s)

emp.count()