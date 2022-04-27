"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """generate serial number, start with 100 or user input"""
        self.start = start
        self.first = True
        self.next_s = start
    
    def __repr__(self):
        """enhanced representation"""
        return f"<SerialGenerator start={self.start} next={self.next_s}>"
    
    def generate(self):
        "return starting number first, then next serial number each time after the first time"
        if not self.first:
            self.next_s += 1
        self.first = False
        # print(self.next_s)
        # self.first is not needed if return self.next_s - 1
        return self.next_s

    def reset(self):
        "reset to starting number"
        self.next_s = self.start
        self.first = True
