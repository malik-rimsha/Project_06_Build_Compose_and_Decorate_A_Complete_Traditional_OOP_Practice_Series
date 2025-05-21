class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The iterator object is the instance itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End iteration
        else:
            num = self.current
            self.current -= 1
            return num

# Usage example
countdown = Countdown(5)

for number in countdown:
    print(number)
