# Create a program that:
# 1. Opens a file named "log.txt" in append mode.
# 2. Adds a new log entry: "Program run successfully".
# 3. Opens the file in read mode and prints all logs.

# Open file in append mode
with open("log.txt", "a") as file:
    file.write("Program run successfully\n")

# Open file in read mode
with open("log.txt", "r") as file:
    print("All Logs:")

    for log in file:
        print(log.strip())
