# Class A with method show()
class A:
    def show(self):
        print("Class A")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("Class B")

# Class C inherits from A and overrides show()
class C(A):
    def show(self):
        print("Class C")

# Class D inherits from B and C (diamond inheritance)
class D(B, C):
    pass

# Create an object of class D
obj = D()

# Call the show() method
obj.show()

# Print the Method Resolution Order (MRO) for class D
print(D.mro())
