# Q8. Concept: Instance & Class Attributes
# Create a class Player with:
# 1. A class variable player_count
# 2. Instance variables name and level
# Track how many players were created.

class Player:
    # Class variable
    player_count = 0

    def __init__(self, name, level):
        # Instance variables
        self.name = name
        self.level = level

        # Increase player count whenever an object is created
        Player.player_count += 1

    def display_details(self):
        print("Player Name:", self.name)
        print("Player Level:", self.level)


# Create player objects
player1 = Player("Noor", 1)
player2 = Player("Ayesha", 5)
player3 = Player("Sara", 3)

# Display player details
player1.display_details()
print()

player2.display_details()
print()

player3.display_details()
print()

# Display total number of players
print("Total Players Created:", Player.player_count)