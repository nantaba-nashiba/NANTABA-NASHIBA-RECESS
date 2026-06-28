import csv
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


DATA_DIR = Path(__file__).parent
CSV_FILE = DATA_DIR / "students.csv"
JSON_FILE = DATA_DIR / "students.json"
LOG_FILE = DATA_DIR / "student_system.log"


class StudentManagementError(Exception):
    """Base exception for the student management system."""
    pass


class InvalidStudentDataError(StudentManagementError):
    """Raised when the student input data is invalid."""
    pass


@dataclass
class StudentRecord:
    registration_number: str
    name: str
    age: int
    gender: str

    def to_csv_row(self) -> Dict[str, str]:
        return {
            "registration_number": self.registration_number,
            "name": self.name,
            "age": str(self.age),
            "gender": self.gender,
        }


def setup_logger() -> None:
    """Configure the logging module for file-based logging."""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.info("Student Record Management system started.")


def log_action(message: str) -> None:
    """Log an informational action taken by the user."""
    logging.info(message)


def log_error(message: str) -> None:
    """Log an error message from the system."""
    logging.error(message)


def ensure_files_exist() -> None:
    """Create CSV and JSON files if they do not exist already."""
    if not CSV_FILE.exists():
        with CSV_FILE.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=["registration_number", "name", "age", "gender"],
            )
            writer.writeheader()
        log_action("Created missing CSV file: students.csv")

    if not JSON_FILE.exists():
        with JSON_FILE.open("w", encoding="utf-8") as json_file:
            json.dump({}, json_file, indent=4)
        log_action("Created missing JSON file: students.json")


def load_students() -> List[StudentRecord]:
    """Load the list of student records from the CSV file."""
    students: List[StudentRecord] = []
    try:
        with CSV_FILE.open("r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if not row.get("registration_number"):
                    continue
                students.append(
                    StudentRecord(
                        registration_number=row["registration_number"].strip(),
                        name=row["name"].strip(),
                        age=int(row["age"]),
                        gender=row["gender"].strip(),
                    )
                )
        log_action("Loaded student records from CSV.")
    except FileNotFoundError:
        log_error("CSV file not found while loading students.")
        raise
    except Exception as error:
        log_error(f"Failed to load students: {error}")
        raise
    return students


def save_students(students: List[StudentRecord]) -> None:
    """Save the student record list back into the CSV file."""
    try:
        with CSV_FILE.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=["registration_number", "name", "age", "gender"],
            )
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_csv_row())
        log_action("Saved student records to CSV.")
    except Exception as error:
        log_error(f"Failed to save students: {error}")
        raise


def load_student_details() -> Dict[str, Dict[str, str]]:
    """Load student details from the JSON file."""
    try:
        with JSON_FILE.open("r", encoding="utf-8") as json_file:
            details = json.load(json_file)
        log_action("Loaded student extra details from JSON.")
    except FileNotFoundError:
        log_error("JSON file not found while loading student details.")
        raise
    except json.JSONDecodeError as error:
        log_error(f"JSON decode error: {error}")
        raise
    except Exception as error:
        log_error(f"Failed to load student details: {error}")
        raise
    return details


def save_student_details(details: Dict[str, Dict[str, str]]) -> None:
    """Write the student details dictionary to the JSON file."""
    try:
        with JSON_FILE.open("w", encoding="utf-8") as json_file:
            json.dump(details, json_file, indent=4)
        log_action("Saved student extra details to JSON.")
    except Exception as error:
        log_error(f"Failed to save student details: {error}")
        raise


def find_student(students: List[StudentRecord], registration_number: str) -> Optional[StudentRecord]:
    """Return a student record by registration number if it exists."""
    registration_number = registration_number.strip().upper()
    return next(
        (student for student in students if student.registration_number.upper() == registration_number),
        None,
    )


def validate_student_data(
    registration_number: str,
    name: str,
    age: str,
    gender: str,
    program: str,
    address: str,
    contact: str,
) -> StudentRecord:
    """Validate student input and convert values to the correct types."""
    if not registration_number.strip():
        raise InvalidStudentDataError("Registration number cannot be empty.")

    if not name.strip():
        raise InvalidStudentDataError("Student name cannot be empty.")

    try:
        age_value = int(age)
    except ValueError:
        raise InvalidStudentDataError("Age must be a whole number.")
    if age_value <= 0:
        raise InvalidStudentDataError("Age must be greater than zero.")

    gender_value = gender.strip().capitalize()
    if gender_value not in {"Male", "Female", "Other"}:
        raise InvalidStudentDataError("Gender must be Male, Female, or Other.")

    if not program.strip():
        raise InvalidStudentDataError("Program cannot be empty.")

    if not address.strip():
        raise InvalidStudentDataError("Address cannot be empty.")

    contact_value = contact.strip()
    if not contact_value.isdigit() or len(contact_value) < 7:
        raise InvalidStudentDataError("Contact must be numeric and at least 7 digits.")

    return StudentRecord(
        registration_number=registration_number.strip().upper(),
        name=name.strip(),
        age=age_value,
        gender=gender_value,
    )


def prompt_student_inputs(existing_registration: Optional[str] = None) -> Dict[str, str]:
    """Prompt the user for student details and return the entered values."""
    print("Enter the student details below. Leave blank to keep the current value when updating.")
    registration_number = existing_registration or input("Registration number: ").strip()
    name = input("Student name: ").strip()
    age = input("Age: ").strip()
    gender = input("Gender (Male/Female/Other): ").strip()
    program = input("Program: ").strip()
    address = input("Address: ").strip()
    contact = input("Contact number: ").strip()
    return {
        "registration_number": registration_number,
        "name": name,
        "age": age,
        "gender": gender,
        "program": program,
        "address": address,
        "contact": contact,
    }


def add_student(students: List[StudentRecord], details: Dict[str, Dict[str, str]]) -> None:
    """Add a new student record and details to the system."""
    try:
        inputs = prompt_student_inputs()
        if find_student(students, inputs["registration_number"]):
            raise InvalidStudentDataError("A student with that registration number already exists.")

        student = validate_student_data(
            inputs["registration_number"],
            inputs["name"],
            inputs["age"],
            inputs["gender"],
            inputs["program"],
            inputs["address"],
            inputs["contact"],
        )

        students.append(student)
        details[student.registration_number] = {
            "program": inputs["program"],
            "address": inputs["address"],
            "contact": inputs["contact"],
        }

        log_action(f"Added student {student.registration_number}: {student.name}")
        print("Student added successfully.")
    except InvalidStudentDataError as error:
        log_error(f"Add student validation failed: {error}")
        print(f"Input error: {error}")
    except Exception as error:
        log_error(f"Unexpected error while adding student: {error}")
        print(f"Unexpected error: {error}")


def display_student(student: StudentRecord, detail: Dict[str, str]) -> None:
    """Print a single student record with its extended details."""
    print("--------------------------------------------")
    print(f"Registration number: {student.registration_number}")
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"Gender: {student.gender}")
    print(f"Program: {detail.get('program', 'N/A')}")
    print(f"Address: {detail.get('address', 'N/A')}")
    print(f"Contact: {detail.get('contact', 'N/A')}")
    print("--------------------------------------------")


def view_all_students(students: List[StudentRecord], details: Dict[str, Dict[str, str]]) -> None:
    """Display all student records in the system."""
    if not students:
        print("No students are currently registered.")
        return
    print("All registered students:")
    for student in students:
        student_details = details.get(student.registration_number, {})
        display_student(student, student_details)
    log_action("Viewed all students.")


def search_student(students: List[StudentRecord], details: Dict[str, Dict[str, str]]) -> None:
    """Search for a student by registration number and print the result."""
    registration_number = input("Enter registration number to search: ").strip().upper()
    if not registration_number:
        print("Registration number cannot be empty.")
        return

    student = find_student(students, registration_number)
    if student is None:
        print("Student not found.")
        log_action(f"Search missed: {registration_number}")
        return

    display_student(student, details.get(student.registration_number, {}))
    log_action(f"Searched for student {registration_number}.")


def update_student(students: List[StudentRecord], details: Dict[str, Dict[str, str]]) -> None:
    """Update an existing student's data."""
    registration_number = input("Enter registration number to update: ").strip().upper()
    student = find_student(students, registration_number)
    if student is None:
        print("Student not found.")
        return

    current_details = details.get(student.registration_number, {})
    print("Leave a field blank to keep the current value.")
    print(f"Current name: {student.name}")
    print(f"Current age: {student.age}")
    print(f"Current gender: {student.gender}")
    print(f"Current program: {current_details.get('program', 'N/A')}")
    print(f"Current address: {current_details.get('address', 'N/A')}")
    print(f"Current contact: {current_details.get('contact', 'N/A')}")

    try:
        name = input("New name: ").strip() or student.name
        age = input("New age: ").strip() or str(student.age)
        gender = input("New gender: ").strip() or student.gender
        program = input("New program: ").strip() or current_details.get("program", "")
        address = input("New address: ").strip() or current_details.get("address", "")
        contact = input("New contact number: ").strip() or current_details.get("contact", "")

        updated_student = validate_student_data(
            student.registration_number,
            name,
            age,
            gender,
            program,
            address,
            contact,
        )

        student.name = updated_student.name
        student.age = updated_student.age
        student.gender = updated_student.gender
        details[student.registration_number] = {
            "program": program,
            "address": address,
            "contact": contact,
        }

        log_action(f"Updated student {student.registration_number}.")
        print("Student details updated successfully.")
    except InvalidStudentDataError as error:
        log_error(f"Update validation failed for {student.registration_number}: {error}")
        print(f"Input error: {error}")
    except Exception as error:
        log_error(f"Unexpected error while updating student {student.registration_number}: {error}")
        print(f"Unexpected error: {error}")


def delete_student(students: List[StudentRecord], details: Dict[str, Dict[str, str]]) -> None:
    """Remove a student record and its matching JSON details."""
    registration_number = input("Enter registration number to delete: ").strip().upper()
    student = find_student(students, registration_number)
    if student is None:
        print("Student not found.")
        return

    confirmation = input(f"Are you sure you want to delete {student.name}? (Y/N): ").strip().upper()
    if confirmation != "Y":
        print("Deletion canceled.")
        return

    students.remove(student)
    details.pop(student.registration_number, None)
    log_action(f"Deleted student {student.registration_number}: {student.name}")
    print("Student record deleted successfully.")


def print_menu() -> None:
    """Print the application menu options."""
    print("\nStudent Record Management System")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Update student details")
    print("5. Delete a student record")
    print("6. Exit")


def main() -> None:
    """Main entry point for the menu-driven application."""
    setup_logger()
    ensure_files_exist()

    students = []
    student_details: Dict[str, Dict[str, str]] = {}

    try:
        students = load_students()
        student_details = load_student_details()

        while True:
            print_menu()
            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                add_student(students, student_details)
            elif choice == "2":
                view_all_students(students, student_details)
            elif choice == "3":
                search_student(students, student_details)
            elif choice == "4":
                update_student(students, student_details)
            elif choice == "5":
                delete_student(students, student_details)
            elif choice == "6":
                print("Exiting the student management system.")
                log_action("User exited the application.")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 6.")
                log_action(f"Invalid menu selection: {choice}")

    except KeyboardInterrupt:
        print("\nThe program interrupted by the user. Saving data before exit.")
        log_action("Program interrupted by user.")
    except Exception as error:
        log_error(f"Fatal error in main loop: {error}")
        print(f"A system error occurred: {error}")
    finally:
        try:
            save_students(students)
            save_student_details(student_details)
            print("Student records saved successfully.")
        except Exception as save_error:
            log_error(f"Failed to save data in finally block: {save_error}")
            print(f"Could not save some data: {save_error}")
        print("Thank you for using the Student Record Management System.")


if __name__ == "__main__":
    main()
