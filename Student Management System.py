class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print("-" * 30)


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        grade = input("Enter Student Grade: ")

        student = Student(student_id, name, age, grade)
        self.students.append(student)
        print("Student Added Successfully!\n")

    def view_students(self):
        if not self.students:
            print("No Students Found.\n")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        student_id = input("Enter Student ID to Search: ")

        for student in self.students:
            if student.student_id == student_id:
                student.display()
                return

        print("Student Not Found.\n")

    def update_student(self):
        student_id = input("Enter Student ID to Update: ")

        for student in self.students:
            if student.student_id == student_id:
                student.name = input("Enter New Name: ")
                student.age = input("Enter New Age: ")
                student.grade = input("Enter New Grade: ")
                print("Student Updated Successfully!\n")
                return

        print("Student Not Found.\n")

    def delete_student(self):
        student_id = input("Enter Student ID to Delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted Successfully!\n")
                return

        print("Student Not Found.\n")


def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()