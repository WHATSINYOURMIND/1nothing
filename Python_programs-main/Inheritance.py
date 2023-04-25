# inheritance
# process to inherits properties from one class to another
# DRY - dont repeat yourself

class Mammal:
    def walk(self):
        print("WALK")


class Dog(Mammal):
    # a class cannot be empty
    # if you want it to go empty then use the pass keyword
    pass


class cat(Mammal):
    def meow(self):
        print("CAT DOES MEOW")


Dog1 = Dog()
Dog1.walk()
cat1 = cat()
cat1.meow()
