# Question:Exception Handling
# Write a program that tries to open "data.txt" in read mode.
# If the file does not exist, catch the exception and print
# "File not found!"

try:
    # Open the file in read mode
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found!")