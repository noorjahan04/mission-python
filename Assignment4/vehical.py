# Q5. Concept: Inheritance
# Create a base class Vehicle with attributes like brand and model.
# Create two subclasses, Car and Bike, that add extra attributes:
# seats (in Car) and engine_cc (in Bike).

# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Child class: Car
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_details(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Number of Seats:", self.seats)

# Child class: Bike
class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_details(self):
        print("Bike Brand:", self.brand)
        print("Bike Model:", self.model)
        print("Engine CC:", self.engine_cc)

# Create objects
car1 = Car("Toyota", "Innova", 7)
bike1 = Bike("Royal Enfield", "Classic 350", 350)

# Display details
print("Car Details:")
car1.display_details()

print("\nBike Details:")
bike1.display_details()