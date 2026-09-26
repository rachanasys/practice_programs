#write a python program To implement Methooverriding
class Employee:
    def work(self):
        print("Employee is doing general work.")
class Developer(Employee):
    def work(self):  # overriding the parent's method
        print("Developer is writing code.")
class Manager(Employee):
    def work(self):  # overriding the parent's method
        print("Manager is managing the team.")
        # Calling the parent's version too, using super()
        super().work()
e = Employee()
d = Developer()
m = Manager()
e.work()
d.work()
m.work()
