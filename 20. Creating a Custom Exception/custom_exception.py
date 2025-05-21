# Define custom exception class
class InvalidAgeError(Exception):
    pass  # We can add custom behavior if needed, but pass is enough here

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

# Using try-except to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid integer for age.")

