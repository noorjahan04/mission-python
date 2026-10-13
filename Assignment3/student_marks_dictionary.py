
students = {}

while True:
    print("\nA. Add a student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students and marks")
    print("E. Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    elif choice == "B":
        name = input("Enter student name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    elif choice == "C":
        name = input("Enter student name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found!")

    elif choice == "D":
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "E":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
