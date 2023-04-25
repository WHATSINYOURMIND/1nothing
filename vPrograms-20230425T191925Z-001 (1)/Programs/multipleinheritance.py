class Base1:
    def __init__(self):
        print("I am in Base1...")

class Base2:
    def __init__(self):
        print("I am in Base2...")

class Derived(Base2,Base1):
    def __init__(self):
        super().__init__()  #First mentioned base class ke method ko call karege
        Base1.__init__(self)
        print("I am in Derived...")

d=Derived()
        

        
