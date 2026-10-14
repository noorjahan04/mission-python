# Q6. Concept: Abstraction
# Create an abstract class Employee with an abstract method
# calculate_salary().
# Create subclasses Intern, FullTimeEmployee, and ContractEmployee
# that implement the method differently.

from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

# Child class: Intern
class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

# Child class: FullTimeEmployee
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# Child class: ContractEmployee
class ContractEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

# Create objects
intern = Intern(10000)
full_time = FullTimeEmployee(50000)
contract = ContractEmployee(160, 300)

# Display salaries
print("Intern Salary:", intern.calculate_salary())
print("Full-Time Employee Salary:", full_time.calculate_salary())
print("Contract Employee Salary:", contract.calculate_salary())