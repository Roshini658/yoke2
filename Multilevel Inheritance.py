class Grandparent:
    def __init__(self,pockets):
        self.pockets=pockets
class Parent(Grandparent):
    def __init__(self,pockets,zips):
        super().__init__(pockets)
        self.zips=zips
class Child(Parent):
    def __init__(self,pockets,zips,material):
        super().__init__(pockets,zips)
        self.material=material
obj1=Child(23,45,"wool")
print(obj1.zips)
print(obj1.material)
print(obj1.pockets)
def show():#Polymorphism (method overriding)
    print("hello how are you")
def show():
    print("i am fine")
show()
class Animal:#method overriding
    def show(self):
        print("hello")
class Person(Animal):
    def show(self):
        print("hi")
obj1=Person()
obj1.show()
class Animal:#duck typing in polymorphism
    def show(self):
        print("hello")
class Person:
    def show(self):
        print("hola bro")
obj1=Animal()
obj2=Person()
obj1.show()
obj2.show()
class Factory:#public attributes and methods
    a="pune"
    def show(self):
        print("hello")
class Bhopal(Factory):
    def show(self):
        print(super().a)
obj1=Bhopal()
obj1.show()
class Bhopal:#protected attributes and methods
    _a="akarsh"
    def _show(self):
        print("hello")
class Pune(Bhopal):
    def show2(self):
        print(super()._a)
obj2=Pune()
obj2._show()
class Person:
    __a="Akarsh"
    def show(self):
        print(Person.__a)
class Animal(Person):
    __b="Sam"
    def slag(self):
        print(super().__a)
obj1=Person()
obj1.show()



