# Q7. Concept: Constructor Overloading (with Default Parameters)
# Create a class Person that allows the constructor to work with:
# 1. Name only
# 2. Name + age
# 3. Name + age + address
# Direct constructor overloading is not supported in Python.
# Use default parameters to simulate constructor overloading.

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age if self.age is not None else "Not provided")
        print("Address:", self.address if self.address is not None else "Not provided")
        print()
        
# Name only
person1 = Person("Noor")

# Name + age
person2 = Person("Ayesha", 23)

# Name + age + address
person3 = Person("Sara", 25, "Bengaluru")

# Display details
print("Person 1 Details:")
person1.display_details()

print("Person 2 Details:")
person2.display_details()

print("Person 3 Details:")
person3.display_details()