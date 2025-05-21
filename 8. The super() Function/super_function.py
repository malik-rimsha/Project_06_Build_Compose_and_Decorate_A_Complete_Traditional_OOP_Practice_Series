class Person:
    def __init__(self, name):
        self.name = name  # Constructor sets the name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling the base class constructor
        self.subject = subject  # Adding the subject field

# Creating an object of the Teacher class
teacher = Teacher("Robbin", "Mathematics")

# Accessing the fields
print("Name:", teacher.name)
print("Subject:", teacher.subject)
