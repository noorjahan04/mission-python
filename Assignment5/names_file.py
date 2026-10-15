# Q1. Concept: File Handling
# 1. Open a file named "names.txt" in write mode.
# 2. Write 5 names entered by the user, one per line.
# 3. Open the same file in read mode and print all names.

# Open the file in write mode
with open("names.txt", "w") as file:
    for i in range(5):
        name = input(f"Enter name {i + 1}: ")
        file.write(name + "\n")

# Open the same file in read mode
with open("names.txt", "r") as file:
    print("\nNames in the file:")
    for name in file:
        print(name.strip())