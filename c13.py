#write a python program To Implement constructor in class
class User:
    def __init__(self, username, role):
        self.username = username  # Initializing properties
        self.role = role
        print(f"User {self.username} created.")

user1 = User("admin_joe", "Administrator")
