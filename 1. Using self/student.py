class Student:
    def __init__(self, name, marks):
        # using self to initialize the attributes
        self.name = name
        self.marks = marks

    def display(self):
        # method to display student details
        print(f"name: {self.name}")
        print(f"marks: {self.marks}")

# Example usage
student1 = Student("John", 85)
student2 = Student("Jane", 90)

# Displaying student details
student1.display()
student2.display()
