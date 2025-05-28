class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP is starting!..."

class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine  

    def start_car(self):
        return f"{self.make} car: {self.engine.start()}"

my_engine = Engine(250)
my_car = Car("Toyota", my_engine)
print(my_car.start_car())
