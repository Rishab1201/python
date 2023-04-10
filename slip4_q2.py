class employee :
    def __init__(self,id,name,department,salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    # def accept(self):
    #     self.id = int(input("Enter ID of Employee : "))
    #     self.name = input("Enter Name of Employee : ")
    #     self.department = input("Enter Department of employee : ")
    #     self.salary = int(input("Enter Salary of employee : "))

    def display(self):
        print(f"\n ID: {self.id} \n Name : {self.name} \n Department : {self.department} \n Salary : {self.salary} \n")
        

class manager(employee):
    def __init__(self, id, name, department, salary, bonus):
        super(manager,self).__init__(id, name, department, salary)
        self.bonus = bonus

    def totalsalary(self):
        print(f"{self.name} got total salary :",self.salary + self.bonus)





id = int(input("Enter ID of Employee : "))
name = input("Enter Name of Employee : ")
department = input("Enter Department : ")
salary = int(input("Enter Salary of Employee : "))
bonus = int(input("Enter bonus of Employee : "))

n = manager(id, name, department, salary, bonus)

m = manager(2, "Rehan", "xyz", 40000, 5000)

n.display()
n.totalsalary()

m.display()
m.totalsalary()




