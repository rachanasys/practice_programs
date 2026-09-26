#write a python program To implement  Multiple Constructors Using @classmethod
import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Alternative constructor taking birth year instead of age
    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.datetime.now().year
        calculated_age = current_year - birth_year
        return cls(name, calculated_age)  # Instantiates and returns the object
# 1. Primary constructor
p1 = Person("John", 30) 
# 2. Alternative constructor
p2 = Person.from_birth_year("Sarah", 1996)
print(f"{p1.name} is {p1.age} years old.")
print(f"{p2.name} is {p2.age} years old.")
