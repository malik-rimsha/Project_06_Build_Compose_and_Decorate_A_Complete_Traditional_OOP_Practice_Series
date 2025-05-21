from abc import ABC, abstractmethod

class Shape(ABC):                           # Abstract class
    @abstractmethod
    def area(self):
        pass                                # Abstract method


class Rectangle(Shape):                     # Inheriting from shape
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height     # Implimenting the Abstract method
    
# creating Rectangle Object
rect = Rectangle(5, 10)
print("Rectangle Area", rect.area())    


