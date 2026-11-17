class Student:
    def __init__(self, usn, name, marks):
        self.usn = usn
        self.name = name
        self.marks = marks

    def display(self):
        print("USN:", self.usn)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("------------------")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        usn = input("enter USN: ")
        for student in self.students:
            if student.usn == usn:
                print("USN already exist!")
                return

        name = input("enter student name: ")
        marks = float(input("enter marks: "))
        new_student = Student(usn, name, marks)
        self.students.append(new_student)
        print("student added successfully")

    def view_student(self):
        if len(self.students) == 0:
            print("no student found!!")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        usn = input("enter USN to search: ")

        for student in self.students:
            if student.usn == usn:
                print("student found!")
                student.display()
                return

        print("student not found!")

    def delete_student(self):
        usn = input("enter USN to delete: ")

        for student in self.students:
            if student.usn == usn:
                self.students.remove(student)
                print("student deleted!")
                return

        print("student not found")


app = StudentManagementSystem()

while True:
    print("\n==========Student Management System========")
    print("1.Add Students")
    print("2.view Students")
    print("3.Search Students")
    print("4.Delete Students")
    print("5.Exit")

    choice = input("enter your choice: ").strip()
    if choice == "1":
        app.add_student()
    elif choice == "2":
        app.view_student()
    elif choice == "3":
        app.search_student()
    elif choice == "4":
        app.delete_student()
    elif choice == "5":
        print("Thank you for using the application!")
        break
    else:
        print("invalid choice try again!")
