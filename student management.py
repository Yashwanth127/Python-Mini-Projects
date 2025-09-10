students = []

def add_student(name, age, grade):
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)

def view_students():
    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")

def search_student(name):
    for s in students:
        if s["name"] == name:
            print(f"Found: {s}")
            return
    print("Student not found")

# Main Program
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        add_student(name, age, grade)

    elif choice == "2":
        view_students()

    elif choice == "3":
        name = input("Enter name to search: ")
        search_student(name)

    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
