#write a python program To Implement Class Variables and Instance Variables
class Employee:
    company_name = "TechCorp"  # Class Variable

    def __init__(self, name):
        self.name = name       # Instance Variable

# Usage
emp1 = Employee("Bob")
emp2 = Employee("Alice")

print(emp1.name, "-", emp1.company_name)
print(emp2.name, "-", emp2.company_name)
