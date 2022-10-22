

class Brand(Car):
    def __init__(self):


class Car:
    def __init__(self,color, miles):
        self.color = color
        self.miles = miles

    def color(self):
        return self.color

    def miles(self):
        return self.miles

    def __str__(self):
        return f"The {self.color} car has {self.miles} miles."


car1 = Car('blue', 20000)

print(car1)