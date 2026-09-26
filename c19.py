#write a python program To Implement Interface Using Abstract Class
from abc import ABC, abstractmethod
class JSONSerializable(ABC):  # Pure Interface
    @abstractmethod
    def to_json(self):
        pass
class Product(JSONSerializable):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_json(self):
        return f'{{"name": "{self.name}", "price": {self.price}}}'
prod = Product("Laptop", 999)
print(prod.to_json())
