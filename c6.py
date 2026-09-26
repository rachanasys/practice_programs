#write a python program To implement Hybrid inheritance
class Person:
    def show_person(self):
        print("This is a Person.")
class Student(Person):
    def show_student(self):
        print("This is a Student.")
class Teacher(Person):
    def show_teacher(self):
        print("This is a Teacher.")
class TeachingAssistant(Student, Teacher):
    def show_ta(self):
        print("This is a Teaching Assistant (Student + Teacher).")
ta = TeachingAssistant()
ta.show_person() ; ta.show_student(); ta.show_teacher() ; ta.show_ta()          
print("\nMethod Resolution Order (MRO):")
for cls in TeachingAssistant.__mro__:
    print(cls.__name__)
    