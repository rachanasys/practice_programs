#write a python program To Implement Static Methods
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
result = Calculator.add(5, 7)
print(f"Addition Result: {result}")
