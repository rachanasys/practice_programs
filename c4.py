#write a python program To implement Multi level inheritance 
class Grandparent:
    def show_grandparent(self):
        print("This is the Grandparent class.")
class Parent(Grandparent):
    def show_parent(self):
        print("This is the Parent class.")
class Child(Parent):
    def show_child(self):
        print("This is the Child class.")
c = Child()
c.show_grandparent()   # inherited from Grandparent
c.show_parent()        # inherited from Parent
c.show_child()         # own method
