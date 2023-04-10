class student :
    def setter(self):
        self.roll = int(input("Enter Roll Number :: "))
        self.name = input("Enter Name of student :: ")
        self.age = int(input("Enter age of student :: "))
        self.gender = input("Enter gender of student :: ")

    def display(self):
        print("Roll Number :: ", self.roll);
        print("Name of student :: ", self.name)
        print("Age of student :: ", self.age)
        print("Gender of student :: ", self.gender)
class test(student):

    def accept(self):
        self.mark1 = int(input("Enter marks of Cpp :: "))
        self.mark2 = int(input("Enter marks of Python :: "))
        self.mark3 = int(input("Enter marks of OOSE :: "))

        self.total = self.mark1 + self.mark2 + self.mark3

    def getter(self):
        print("Marks of Cpp :: ",self.mark1);
        print("Marks of Python :: ",self.mark2)
        print("Marks of OOSE :: ",self.mark3);
        print("Total marks :: ",self.total);

obj = test()

obj.setter()
obj.accept()
obj.display()
obj.getter()

obj1 = test()

obj1.setter()
obj1.accept();
obj1.display();
obj1.getter();

obj2 = test()

obj2.setter()
obj2.accept();
obj2.display();
obj2.getter();
