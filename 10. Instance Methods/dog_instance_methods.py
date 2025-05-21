# Define the Dog class
class Dog:
    # Constructor to initialize instance variables
    def __init__(self, name, breed):
        self.name = name  # Instance variable: name
        self.breed = breed  # Instance variable: breed
    
    # Instance method to print a message
    def bark(self):
        print(f"Woof! My name is {self.name}, and I am a {self.breed}.")

# Create an object of the Dog class
my_dog = Dog("Bruno", "Labrador")

# Call the bark method
my_dog.bark()
