students = []


def add_student(name, roll_no):
    student = {
        "name": name,
        "roll_no": roll_no
    }
    students.append(student)
    print("Student added successfully!")


def display_students():
    print("\nStudent List:")

    for student in students:
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])

def find_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student Found!")
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            return

    print("Student not found.")

# Main program
add_student("Nandan", "101")
add_student("Rahul", "102")

display_students()