# Define the Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

# Define the Department class
class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # List to store references to Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)  # Add an Employee object to the list

    def display_employees(self):
        print(f"Department: {self.dept_name}")
        if self.employees:
            for emp in self.employees:
                print(emp.get_details())
        else:
            print("No employees in this department.")

# Create Employee objects
emp1 = Employee("Alice", 101)
emp2 = Employee("Bob", 102)

# Create a Department object
dept = Department("Human Resources")

# Add employees to the department
dept.add_employee(emp1)
dept.add_employee(emp2)

# Display employees in the department
dept.display_employees()
