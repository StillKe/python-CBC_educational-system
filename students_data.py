import json

class Student:
    next_id = 1  # Class variable to keep track of next available ID

    def __init__(self, name, grade, transport=False, meals=False):
        self.name = name
        self.grade = grade
        self.transport = transport
        self.meals = meals
        self.student_id = Student.next_id
        Student.next_id += 1

    def calculate_total_fee(self, base_fee):
        total_fee = base_fee
        if self.transport:
            total_fee += 2000  # Additional fee for transport
        if self.meals:
            total_fee += 1000  # Additional fee for meals
        return total_fee

    def to_dict(self):
        return {
            'name': self.name,
            'grade': self.grade,
            'transport': self.transport,
            'meals': self.meals,
            'student_id': self.student_id
        }

def save_students_to_file(file_path, students):
    students_data = [student.to_dict() for student in students]
    with open(file_path, 'w') as file:
        json.dump(students_data, file, indent=4)

def load_students_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            students_data = json.load(file)
        students = [Student(student['name'], student['grade'], student['transport'], student['meals']) for student in students_data]
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"File '{file_path}' not found or empty. Creating a new file.")
        students = []
        save_students_to_file(file_path, students)
    return students

def collect_student_data():
    students = []
    while True:
        name = input("Enter student's name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        grade = input("Enter student's grade: ")
        transport = input("Does the student require transportation? (yes/no): ").lower() == 'yes'
        meals = input("Does the student require meals? (yes/no): ").lower() == 'yes'
        student = Student(name, grade, transport, meals)
        students.append(student)
    return students

# Example usage
if __name__ == "__main__":
    print("Welcome to the Educational System Python program!")
    print("This program implements a simple educational system model inspired by the Competency-Based Curriculum (CBC).")

    # Prompt user to enter student data
    students = collect_student_data()

    # Save students to a JSON file
    file_path = "students.json"
    save_students_to_file(file_path, students)
    print(f"Student data saved to '{file_path}'.")

    # Load students from file
    loaded_students = load_students_from_file(file_path)
    print("Loaded student data:")
    for student in loaded_students:
        print(f"Name: {student.name}, Grade: {student.grade}, Transportation: {student.transport}, Meals: {student.meals}")
