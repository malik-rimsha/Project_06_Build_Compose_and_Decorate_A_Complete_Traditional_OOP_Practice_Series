# Define the TemperatureConverter class
class TemperatureConverter:
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32  # Conversion formula

# Example usage of the static method
temp_celsius = 25  # Temperature in Celsius
temp_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_celsius)

print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F.")
