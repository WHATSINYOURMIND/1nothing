class complex:
    def accept(self):
        self.x=int(input("Enter real term="))
        self.y=int(input("Enter imaginary term="))
    def display(self):
        print(self.x,"+i",self.y)
    def add(self,a,b):
        self.x=a.x+b.x
        self.y=a.y+b.y

c1=complex()
c2=complex()
c3=complex()
c1.accept()
c1.display()
c2.accept()
c2.display()
c3.add(c1,c2)
print("Addition=")
c3.display()
