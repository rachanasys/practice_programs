#write a python program To implement Polymorphism
class Bird:
    def sound(self):
        print("Some generic bird sound.")
class Sparrow(Bird):
    def sound(self):
        print("Sparrow says: Chirp chirp!")
class Crow(Bird):
    def sound(self):
        print("Crow says: Caw caw!")
birds = [Bird(), Sparrow(), Crow()]
# Same method call, different behaviour depending on the object
for b in birds:
    b.sound()
    # Polymorphism also works with built-in functions
print(len("Hello"))       # length of a string
print(len([1, 2, 3, 4]))  # length of a list
