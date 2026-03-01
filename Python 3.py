students = []

def add_student():
    name = input("Enter Student Name: ")
    while True:
        try:
            marks = float(input("Enter Marks: "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    students.append({"name": name, "marks": marks})
    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No students recorded yet.")
    else:
        print("Student List:")
        for i, s in enumerate(students, start=1):
            print(f"{i}. {s['name']}: {s['marks']}")

def search_student():
    if not students:
        print("No students recorded yet.")
    else:
        query = input("Search by ID (number) or Name: ")
        try:
            query_id = int(query) - 1
            if 0 <= query_id < len(students):
                s = students[query_id]
                print(f"Name: {s['name']}, Marks: {s['marks']}")
            else:
                print("Student not found.")
        except ValueError:
            found = [s for s in students if s['name'].lower() == query.lower()]
            if found:
                for s in found:
                    print(f"Name: {s['name']}, Marks: {s['marks']}")
            else:
                print("Student not found.")

def display_stats():
    if not students:
        print("No students recorded yet.")
    else:
        avg_marks = sum(s['marks'] for s in students) / len(students)
        topper = max(students, key=lambda s: s['marks'])
        print(f"Topper: {topper['name']}")
        print(f"Average Marks: {avg_marks:.2f}")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Display Stats")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            display_stats()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()