# Define the decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")  # Additional behavior before function call
        func()  # Call the original function
    return wrapper

# Define the original function
@log_function_call  # Apply the decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
