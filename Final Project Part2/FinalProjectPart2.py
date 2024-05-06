# Prabhu Roka
# 1986444
import csv
from datetime import datetime


class Student:
    def __init__(self, student_id, last_name, first_name, major, disciplinary_action=False):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.disciplinary_action = disciplinary_action


class UniversityRecords:
    def __init__(self):
        self.students = {}
        self.gpa_records = {}
        self.graduation_dates = {}

    # method to read data from the files
    def load_data(self, students_file, gpa_file, graduation_dates_file):
        # Read student records
        with open(students_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                student_id, last_name, first_name, major, *disciplinary_action = row
                disciplinary_action = disciplinary_action[0].upper() if disciplinary_action else False
                self.students[student_id] = Student(student_id, last_name,
                                                    first_name, major, disciplinary_action == 'Y')

        # Read GPA records
        with open(gpa_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                student_id, gpa = row
                self.gpa_records[student_id] = float(gpa)

        # Read graduation dates
        with open(graduation_dates_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                student_id, graduation_date = row
                self.graduation_dates[student_id] = datetime.strptime(graduation_date, "%m/%d/%Y").date()

    # Method to query the results
    def query_students(self, major, target_gpa):
        print("Querying for major:", major, target_gpa)

        # Get the current date
        current_date = datetime.now().date()

        # Initialize variables to track closest GPA and its corresponding student
        closest_student = None
        closest_gpa_difference = float('inf')

        matching_students = []  # Students within 0.10 of the requested GPA
        close_students = []  # Students within 0.25 of the requested GPA

        for student_id, student in self.students.items():
            if student.major.lower() == major.lower() and not student.disciplinary_action:
                student_gpa = self.gpa_records.get(student_id, 0)
                gpa_difference = abs(student_gpa - target_gpa)  # Calculate gpa difference

                # Condition for the student gpa within 0.1 difference
                if gpa_difference <= 0.1:
                    graduation_date = self.graduation_dates.get(student_id)
                    if graduation_date and graduation_date >= current_date:
                        matching_students.append(student)
                # Condition for the student gpa within 0.25 difference
                elif gpa_difference <= 0.25:
                    graduation_date = self.graduation_dates.get(student_id)
                    if graduation_date and graduation_date >= current_date:
                        close_students.append(student)

                # Update closest student if applicable
                if gpa_difference < closest_gpa_difference:
                    closest_student = student
                    closest_gpa_difference = gpa_difference

        # If no matching or close students, print the student with the closest GPA
        if not matching_students and not close_students:
            if closest_student:
                print("No students found within 0.25 of the requested GPA.")
                print("Closest student:")
                print(f"Student ID: {closest_student.student_id}, "
                      f"Name: {closest_student.first_name} {closest_student.last_name}, "
                      f"GPA: {self.gpa_records.get(closest_student.student_id, 'N/A')}")

        # Print matching students if any
        if matching_students:
            print("Your student(s):")
            for student in matching_students:
                print(
                    f"Student ID: {student.student_id}, Name: {student.first_name} "
                    f"{student.last_name}, GPA: {self.gpa_records.get(student.student_id, 'N/A')}")

        # Print close students if any
        if close_students:
            print("You may also consider:")
            for student in close_students:
                print(
                    f"Student ID: {student.student_id}, Name: {student.first_name} "
                    f"{student.last_name}, GPA: {self.gpa_records.get(student.student_id, 'N/A')}")


def main():
    # Assigning class and their data to variable
    university_records = UniversityRecords()
    university_records.load_data("StudentsMajorsList.csv", "GPAList.csv", "GraduationDatesList.csv")

    while True:
        query = input("Enter major and GPA (e.g., 'Computer Science 3.5'), or 'q' to quit: ").strip()
        if query.lower() == 'q':
            break
        else:
            # This code will not work with other format than simple major and then gpa (For ex. Computer Science 3.5).
            parts = query.split()
            if len(parts) >= 2:
                # Check if the last part can be converted to a float
                try:
                    target_gpa = float(parts[-1])     # Last part as the gpa
                    major = ' '.join(parts[:-1])  # Combine all parts except the last one as major
                    university_records.query_students(major, target_gpa)
                except ValueError:
                    print("Invalid input. Please enter major and GPA in the correct format.")
            else:
                print("Invalid input. Please enter major and GPA in the correct format.")


# Calling the main function
if __name__ == "__main__":
    main()
