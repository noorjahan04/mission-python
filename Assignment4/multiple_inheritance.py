# Q9. Concept: Multiple Inheritance
# Create the following classes: Herbivore, Carnivore, and Omnivore
# with some attributes and methods.
# Then create a class Bear that inherits from all the above
# classes to showcase how multiple inheritance works.


# Parent class 1
class Herbivore:
    def __init__(self):
        self.plant_food = "Grass and Fruits"

    def eat_plants(self):
        print("Herbivore eats:", self.plant_food)

# Parent class 2
class Carnivore:
    def __init__(self):
        self.meat_food = "Meat and Fish"

    def eat_meat(self):
        print("Carnivore eats:", self.meat_food)

# Parent class 3
class Omnivore:
    def __init__(self):
        self.food_type = "Plants and Meat"

    def eat_both(self):
        print("Omnivore eats:", self.food_type)

# Child class: Multiple Inheritance
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        Herbivore.__init__(self)
        Carnivore.__init__(self)
        Omnivore.__init__(self)
        self.name = name

    def display_details(self):
        print("Animal Name:", self.name)

# Create object
bear1 = Bear("Brown Bear")

# Display details
bear1.display_details()

# Access methods from all parent classes
bear1.eat_plants()
bear1.eat_meat()
bear1.eat_both()