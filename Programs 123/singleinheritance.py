class person:
    def __init__(self):
        self.id=int(input("Enter ID="))
        self.name=input("Enter Name=")
    def display(self):
        print("ID=",self.id," Name=",self.name)

class employee(person):
    def __init__(self): #Method Overriding
        person.__init__(self)   #super().__init__()
        self.salary=int(input("Enter Salary="))
    def display(self):
        person.display(self)    #super().display()
        print("Salary=",self.salary)
        
e=employee()
e.display()

        
