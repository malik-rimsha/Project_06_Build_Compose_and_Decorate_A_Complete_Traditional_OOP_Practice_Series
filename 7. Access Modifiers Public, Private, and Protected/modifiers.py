class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name                # Public Variable
        self._salary = salary           # Protecred Variable
        self.__ssn = ssn                 # Private Variable

# Creating an Object
emp = Employee ("Marshal", 60510000, 568-15-4456)

# Accesing the Variables
print("Public Name:", emp.name)          # Accessable Directly
print("Protected Salary:", emp._salary)  # Accessable but conventionally Protected
try:
    print("Privat SSN:", emp.__ssn)       # Not Directly Accessable, raises an error
except AttributeError:
    print("Privat SSN cannot be accessd directly!")
