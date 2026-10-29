students = {}


def add_student(student_id, name, marks):
    if not student_id:
        raise ValueError("Student ID cannot be empty")

    if not name.strip():
        raise ValueError("Student name cannot be empty")

    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    if student_id in students:
        raise ValueError("Student ID already exists")

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    return "Student added successfully"


def get_student(student_id):
    return students.get(student_id)


def get_all_students():
    return students


def delete_student(student_id):
    if student_id not in students:
        return False

    del students[student_id]
    return True


if __name__ == "__main__":
    print("Student Management System")

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                marks = float(input("Enter marks: "))

                print(add_student(student_id, name, marks))

            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            print(get_all_students())

        elif choice == "3":
            student_id = input("Enter student ID: ")
            print(get_student(student_id))

        elif choice == "4":
            student_id = input("Enter student ID: ")

            if delete_student(student_id):
                print("Student deleted successfully")
            else:
                print("Student not found")

        elif choice == "5":
            print("Exiting application")
            break

        else:
            print("Invalid choice")