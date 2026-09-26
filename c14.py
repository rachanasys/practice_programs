#write a python program To Implement destructor in class
class DatabaseConnection:
    def __init__(self):
        print("Database connection opened.")

    def __del__(self):
        print("Database connection closed cleanly.")

conn = DatabaseConnection()
del conn  # Manually deleting the object to trigger destructor
