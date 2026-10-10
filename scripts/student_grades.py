# Student Grades Management Program

students = {
    "Rahul": "A",
    "Priya": "B",
    "Aman": "C"
}

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Display all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()
        grade = input("Enter student grade (A, B, C, D, F): ").strip().upper()

        if not name:
            print("Student name cannot be empty.")
        elif grade not in ["A", "B", "C", "D", "F"]:
            print("Invalid grade. Please enter A, B, C, D, or F.")
        elif name in students:
            print("Student already exists. Choose update instead.")
        else:
            students[name] = grade
            print("Student added successfully.")

    elif choice == "2":
        name = input("Enter the student name to update: ").strip()

        if name in students:
            grade = input("Enter the new grade (A, B, C, D, F): ").strip().upper()

            if grade in ["A", "B", "C", "D", "F"]:
                students[name] = grade
                print("Grade updated successfully.")
            else:
                print("Invalid grade.")
        else:
            print("Student not found.")

    elif choice == "3":
        if students:
            print("\n--- All Student Grades ---")
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No students found.")

    elif choice == "4":
        print("Exiting Student Grades Program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
