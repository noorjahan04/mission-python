# 1. Has a list of numbers: [5, 10, 15, 20, 25]
# 2. Uses a list comprehension to create a new list
#    with only numbers greater than 15.
# 3. Prints the new list.

# Original list
numbers = [5, 10, 15, 20, 25]

# Create a new list using list comprehension
new_list = [num for num in numbers if num > 15]

# Print the new list
print("Numbers greater than 15:", new_list)
