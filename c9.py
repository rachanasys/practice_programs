#write a python program To implement Method over loading
from functools import singledispatchmethod
# ---- Approach 1: simulate overloading using default/variable arguments ----
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
# ---- Approach 2: using *args for flexible number of arguments ----
class Adder:
    def add(self, *args):
        return sum(args)
# ---- Approach 3: true overload-like behaviour using singledispatchmethod
#      (dispatches based on the type of the first argument) ----
class Printer:
    @singledispatchmethod
    def show(self, value):
        print(f"Generic value: {value}")
    @show.register
    def _(self, value: int):
        print(f"Integer value: {value}")
    @show.register
    def _(self, value: str):
        print(f"String value: {value}")
calc = Calculator()
print("Calculator.add(2):", calc.add(2))
print("Calculator.add(2, 3):", calc.add(2, 3))
print("Calculator.add(2, 3, 4):", calc.add(2, 3, 4))
adder = Adder()
print("Adder.add(1,2,3,4):", adder.add(1, 2, 3, 4))
p = Printer()
p.show(10)          # dispatches to int version
p.show("hello")     # dispatches to str version
p.show(3.14)        # dispatches to generic version
