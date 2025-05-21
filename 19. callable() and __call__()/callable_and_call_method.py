class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the multiplication factor

    def __call__(self, number):
        return number * self.factor  # Multiply input by factor

# Create an instance with factor 5
multiplier = Multiplier(5)

# Check if the instance is callable
print(callable(multiplier))  # Expected output: True

# Use the instance like a function
result = multiplier(10)  # 10 * 5 = 50
print(result)  # Expected output: 50
