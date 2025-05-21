class Car:
    def __init__(self, brand):
        #public variable
        self.brand = brand

        def strat(self):
            #public method
            print(f"The Car {self.brand} has started.")

# Instantiat the class
car1 = Car("Toyota")
car2 = Car("Honda")

# Accessing the variable
print(f"Car 1 Brand: {car1.brand}")
print(f"Car 2 Brand: {car2.brand}")

# Calling the Public method
car1.start()
car2.start()