class Logger:
    # Constructor
    def __init__(self):
        print("Logger object created!")

    # Destructor
    def __del__(self):
        print("Logger object destroyed!")

# Object creation
log1 = Logger()

# Object destruction by deleting explicitly
del log1
