# Question: JSON File Handling
# Create a Python dictionary of 3 cities and their populations.
# Save it to "cities.json".
# 1. Load the JSON and print each city and its population.
# 2. Ask the user for a new city and its population.
#    Update this information in the JSON file.

import json

# Create a dictionary of 3 cities and their populations
cities = {
    "Bengaluru": 13000000,
    "Hyderabad": 10000000,
    "Mumbai": 21000000
}

# Save the dictionary to a JSON file
with open("cities.json", "w") as file:
    json.dump(cities, file, indent=4)

# Load the JSON file
with open("cities.json", "r") as file:
    cities = json.load(file)

# Print each city and its population
print("City Populations:")
for city, population in cities.items():
    print(city, ":", population)

# Ask the user for a new city and its population
new_city = input("\nEnter a new city: ")
new_population = int(input("Enter its population: "))

# Update the dictionary
cities[new_city] = new_population

# Save the updated dictionary to the JSON file
with open("cities.json", "w") as file:
    json.dump(cities, file, indent=4)

print("\nCity information updated successfully!")
print(cities)
