# Q3. Concept: Encapsulation
# Create a class Student with private attributes __name, __roll_no,
# and __marks. Provide getter and setter methods with validation.
# Marks cannot be negative, roll number must be between 1 and 100,
# and name cannot be empty.

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    # Getter methods
    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    # Setter method for name
    def set_name(self, name):
        if name.strip() != "":
            self.__name = name
        else:
            print("Name cannot be empty")

    # Setter method for roll number
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100")

    # Setter method for marks
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks cannot be negative")


# Create a Student object
student1 = Student("Noor", 10, 85)

# Display student details
print("Student Name:", student1.get_name())
print("Roll Number:", student1.get_roll_no())
print("Marks:", student1.get_marks())

# Update student details using setter methods
student1.set_name("Noor Jahan")
student1.set_roll_no(20)
student1.set_marks(95)

# Display updated details
print("\nUpdated Student Details:")
print("Student Name:", student1.get_name())
print("Roll Number:", student1.get_roll_no())
print("Marks:", student1.get_marks())

# Test validation
student1.set_name("")
student1.set_roll_no(150)
student1.set_marks(-10)