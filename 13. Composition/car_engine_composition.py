# Define the Engine class
class Engine:
    def start(self):
        print("Engine started.")

# Define the Car class
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        self.engine.start()  # Access Engine's start method

# Create an Engine object
my_engine = Engine()

# Pass the Engine object to the Car class
my_car = Car(my_engine)

# Start the car, which starts the engine
my_car.start_car()
