#write a python program To Implement encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount!")
account = BankAccount("Alice", 1000)
print(f"Initial Balance: {account.balance}")
account.balance = 1500  # Updates via setter
print(f"Updated Balance: {account.balance}")
