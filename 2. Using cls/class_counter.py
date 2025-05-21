class Counter:
    #class variable to keep track of the object count
    object_count = 0

    def __init__(self):
        # Increment the count whenever an object is created
        Counter.object_count += 1

    @classmethod
    def display_count(cls):
        # class method to display the object count
        print(f"Numbers of object created: {cls.object_count}")

# creating objects
object1 = Counter()
object2 = Counter()
object3 = Counter()  

# Displaying the count using the class method
Counter.display_count()