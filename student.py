class Student:
    def __init__(self, name, student_id, student_class):
        self.name = name
        self.student_id = student_id
        self.student_class = student_class
        self.courses = []

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course.title}.")

    def __str__(self):
        return f"Student Name: {self.name}\nStudent ID: {self.student_id}\nClass: {self.student_class}\nCourses Enrolled: {', '.join([course.title for course in self.courses])}"


class Class:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees
        self.students = []

    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} enrolled in {self.name}.")

    def calculate_total_fee(self):
        total_fee = self.fees
        return total_fee

    def __str__(self):
        return f"Class Name: {self.name}\nClass Fees: KES {self.fees}\nNumber of Students Enrolled: {len(self.students)}"


# Example usage
if __name__ == "__main__":
    # Define classes and their fees
    classes = {
        "Baby Class": 5000,
        "PP1": 6000,
        "PP2": 6500,
        "Grade 1": 7000,
        "Grade 2": 7200,
        "Grade 3": 7500,
        "Grade 4": 7700,
        "Grade 5": 8000,
        "Grade 6": 8200,
        "Grade 7": 8500
    }

    # Create instances of Class
    class_objects = {class_name: Class(class_name, fees) for class_name, fees in classes.items()}

    # Prompt user to enroll students
    while True:
        student_name = input("Enter student's name (or 'q' to quit): ")
        if student_name.lower() == 'q':
            break
        student_id = input("Enter student's ID: ")
        student_class = input("Enter student's class (e.g., Baby Class, PP1, Grade 1, etc.): ")

        # Check if the entered class exists
        if student_class in class_objects:
            # Create Student instance
            student = Student(student_name, student_id, student_class)

            # Enroll student in the respective class
            class_objects[student_class].enroll_student(student)
        else:
            print("Invalid class name. Please enter a valid class.")

    # Display class information
    print("\nClass Information:")
    for class_obj in class_objects.values():
        print(class_obj)
        print()

    # Calculate total fees for each class
    print("\nTotal Fees for Each Class:")
    for class_obj in class_objects.values():
        total_fee = class_obj.calculate_total_fee()
        print(f"{class_obj.name}: KES {total_fee}")
