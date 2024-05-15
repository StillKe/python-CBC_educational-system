import os
import json

class Student:
    next_id = 1  # Class variable to keep track of next available ID

    def __init__(self, first_name, middle_name, last_name, student_class, transport=False, tea_and_snacks=False, lunch=False):
        self.name = f"{first_name} {middle_name} {last_name}"
        self.student_id = Student.next_id  # Assign the next available ID
        Student.next_id += 1  # Increment next available ID
        self.student_class = student_class
        self.transport = transport
        self.tea_and_snacks = tea_and_snacks
        self.lunch = lunch

    def calculate_total_fee(self, base_fee):
        total_fee = base_fee
        if self.transport:
            total_fee += 2000  # Additional fee for transport
        if self.tea_and_snacks:
            total_fee += 500   # Additional fee for tea and snacks
        if self.lunch:
            total_fee += 1000  # Additional fee for lunch
        return total_fee

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Class: {self.student_class}"


def load_students_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            students = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"File '{file_path}' not found or empty. Creating a new file.")
        students = {}
        save_students_to_files(students)
    return students


def save_students_to_files(students):
    for student in students.values():
        grade_directory = f"students/{student['student_class']}"
        os.makedirs(grade_directory, exist_ok=True)
        file_path = f"{grade_directory}/{student['name'].replace(' ', '_')}.json"
        with open(file_path, 'w') as file:
            json.dump(student, file, indent=4)


def collect_student_data():
    students = {}
    while True:
        first_name = input("Enter student's first name (or 'q' to quit): ")
        if first_name.lower() == 'q':
            break
        
        middle_name = input("Enter student's middle name: ")
        
        last_name = input("Enter student's last name: ")
        
        while True:
            student_class = input("Enter student's class (e.g., Baby Class, PP1, Grade 1, etc.): ").strip().title()
            if student_class.lower() in ["baby class", "pp1", "pp2", "grade 1", "grade 2", "grade 3", "grade 4", "grade 5", "grade 6", "grade 7"]:
                break
            print("Invalid class name. Please enter a valid class.")
        
        transport = input("Does the student require transport? (yes/no): ").strip().lower()
        while transport not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            transport = input("Does the student require transport? (yes/no): ").strip().lower()
        
        tea_and_snacks = input("Does the student partake in 10 o'clock tea and snacks? (yes/no): ").strip().lower()
        while tea_and_snacks not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            tea_and_snacks = input("Does the student partake in 10 o'clock tea and snacks? (yes/no): ").strip().lower()
        
        lunch = input("Does the student take lunch at school? (yes/no): ").strip().lower()
        while lunch not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            lunch = input("Does the student take lunch at school? (yes/no): ").strip().lower()
        
        student = {
            'name': f"{first_name} {middle_name} {last_name}",
            'student_class': student_class,
            'transport': transport == 'yes',
            'tea_and_snacks': tea_and_snacks == 'yes',
            'lunch': lunch == 'yes'
        }
        students[student['name']] = student
    return students


# Example usage
if __name__ == "__main__":
    # Prompt user to enter student data
    students = collect_student_data()

    # Save students to files according to their grade
    save_students_to_files(students)
