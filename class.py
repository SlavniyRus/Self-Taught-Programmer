import math

class Circle():
    def __init__(self, r):
        self.radius = r
        print("Circle add")
    def area(self):
        return math.pi * self.radius **2
