#Write a program to implement inheritance 
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

d = Dog("Rex")
d.eat()      # inherited method
d.sleep()    # inherited method
d.bark()     # own method
