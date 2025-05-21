class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        """Getter method: Get the price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter method: Set the price, with validation."""
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter method: Delete the price."""
        print("Deleting price...")
        del self._price

# Usage example
p = Product(100)

# Access price using getter
print(p.price)  # Output: 100

# Update price using setter
p.price = 150
print(p.price)  # Output: 150

# Delete price using deleter
del p.price

# Trying to access price after deletion will raise an AttributeError
# print(p.price)  # Uncommenting this will cause an error
