import json

class Student:
    next_id = 1  # Class variable to keep track of next available ID

    def __init__(self, name, student_class):
        self.name = name
        self.student_class = student_class
        self.student_id = Student.next_id
        Student.next_id += 1

    def to_dict(self):
        return {
            'name': self.name,
            'student_class': self.student_class,
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
        students = [Student(student['name'], student['student_class']) for student in students_data]
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"File '{file_path}' not found or empty. Creating a new file.")
        students = []
        save_students_to_file(file_path, students)
    return students

# Example usage
if __name__ == "__main__":
    students = [
        Student("John Doe", "Grade 7"),
        Student("Alice Smith", "Grade 5"),
        Student("Bob Johnson", "Grade 3")
    ]

    file_path = "students.json"
    save_students_to_file(file_path, students)

    # Load students from file
    loaded_students = load_students_from_file(file_path)
    for student in loaded_students:
        print(student.name, student.student_class)
