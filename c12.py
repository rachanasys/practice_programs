#write a python program To Implement abstraction
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started. Vroom!"
my_car = Car()
print(my_car.start_engine())
