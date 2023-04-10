class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Employee(Person):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.salary = salary

n = int(input('Enter Number of Employees : ')) # number of employees to create
employees = []  # create an empty list to store the employees

for i in range(n):
    name = input("Enter employee name: ")
    address = input("Enter employee address: ")
    salary = input("Enter employee salary: ")
    emp = Employee(name, address, salary)
    employees.append(emp)

# print the details of each employee
for emp in employees:
    print(f"Name: {emp.name}, Address: {emp.address}, Salary: {emp.salary}")
