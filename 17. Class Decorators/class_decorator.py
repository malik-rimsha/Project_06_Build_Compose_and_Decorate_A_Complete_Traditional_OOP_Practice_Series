# Define the class decorator
def add_greeting(cls):
    # Define the new method
    def greet(self):
        return "Hello from Decorator!"
    # Add the new method to the class
    cls.greet = greet
    return cls

# Define the original class without greet()
@add_greeting  # Apply the class decorator
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of Person
p = Person("Alice")

# Call the new greet() method added by the decorator
print(p.greet())
