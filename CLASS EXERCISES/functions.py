def display_student_info(name, age, course, student_number):
    """Display a student's name, age, course, and student number."""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Student Number: {student_number}")


if __name__ == "__main__":
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")
    student_number = input("Enter student number: ")

    display_student_info(name, age, course, student_number)

