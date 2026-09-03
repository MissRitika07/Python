##Destructor in Python
# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Constructor called")

#     def __del__(self):
#         print("Destructor called")

# student1 = Student("Ritika")

# del student1

##single inheritance
##One parent → One child
class Maths:
    def addition(self):
        print("Maths addition")

class Algebra(Maths):
    def equation(self):
        print("Algebra equation")

a = Algebra()
a.addition()
a.equation()

##multiple inheritance 
##Two parents → One child
class Maths:
    def addition(self):
        print("Maths addition")

class Science:
    def experiment(self):
        print("Science experiment")

class Engineering(Maths, Science):
    pass

e = Engineering()
e.addition()
e.experiment()

##multilevel inheritance 
##A class inherits from another child class, forming a chain.

class Science:
    def study(self):
        print("Science subject")

class Physics(Science):
    def theory(self):
        print("Physics theory")

class Mechanics(Physics):
    def practical(self):
        print("Mechanics practical")

m = Mechanics()
m.study()
m.theory()
m.practical()

# Hierarchical Inheritance

# Multiple child classes inherit from the same parent class.

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()

# Hybrid Inheritance

# Combination of two or more type

class Science:
    def study(self):
        print("Science subject")

class Physics(Science):
    def physics(self):
        print("Physics")

class Chemistry(Science):
    def chemistry(self):
        print("Chemistry")

class Engineering(Physics, Chemistry):
    def project(self):
        print("Engineering project")

e = Engineering()
e.study()
e.physics()
e.chemistry()
e.project()

##Access Specifiers in Python
class Parent:
    name = "Ritika"        # Public
    _marks = 90            # Protected
    __age = 20             # Private

    def show_parent(self):
        print("Public:", self.name)
        print("Protected:", self._marks)
        print("Private:", self.__age)


class Child(Parent):
    def show_child(self):
        print("Public:", self.name)
        print("Protected:", self._marks)
        # print(self.__age)  # Error: private member


c = Child()

c.show_parent()
c.show_child()

print(c.name)      # Public → accessible
print(c._marks)    # Protected → accessible
# print(c.__age)   # Private → not directly accessible