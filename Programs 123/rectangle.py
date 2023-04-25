class rectangle:
    def accept(self):
        self.length=int(input("Enter length="))
        self.breadth=int(input("Enter breadth="))
    def area(self):
        a=self.length*self.breadth
        print("Area of rectangle=",a)

r1=rectangle()
r1.accept()
r1.area()
r2=rectangle()
r2.accept()
r2.area()
