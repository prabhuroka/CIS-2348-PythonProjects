# Prabhu Roka
# 1986444
import csv
from datetime import datetime


# class student to include all the properties of a student
class Student:
    def __init__(self, student_id, last_name, first_name, major, disciplinary_action=False):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.disciplinary_action = disciplinary_action
        self.gpa = None
        self.graduation_date = None


# function to read the data from csv file.
def read_csv(filename):
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        # loop to append the data to the list data
        for row in reader:
            data.append(row)
    return data


# defining process_students function to process all the data read from the input files and prepare them for output data.
def process_students(students_data, gpa_data, graduation_data):
    students = {}
    for student_row in students_data:
        # assigning the data returned from the student's data file.
        student_id, last_name, first_name, major, disciplinary_action = student_row
        # Assigning the class Student properties to the variable student
        student = Student(student_id, last_name, first_name, major, disciplinary_action)
        students[student_id] = student

    for gpa_row in gpa_data:
        # assigning the data returned from the gpa_data's file.
        student_id, gpa = gpa_row
        # condition to check if there is student id and if true assign the gpa to the data.
        if student_id in students:
            students[student_id].gpa = float(gpa)

    for graduation_row in graduation_data:
        # assigning the data returned from the graduation_data's file.
        student_id, graduation_date = graduation_row
        if student_id in students:
            students[student_id].graduation_date = graduation_date
    # all the values of the student is returned
    return list(students.values())


# function to sort the data by student id.
def sort_by_student_id(student):
    return student.student_id


# function to sort the data by student last name.
def sort_by_student_last_name(student):
    return student.last_name


# function to sort the data by student graduation date.
def sort_by_graduation_date(student):
    return student.graduation_date


# function to sort the data by student gpa.
def sort_by_gpa(student):
    return student.gpa


# function to write all the data properties to a file
def write_full_roster(students, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Major", "First Name",
                         "Last Name", "GPA", "Graduation Date", "Disciplinary Action"])
        # sorting the students by student last name.
        sorted_students = sorted(students, key=sort_by_student_last_name)
        # writing sorted student's data properties to a file
        for student in sorted_students:
            writer.writerow([student.student_id, student.major, student.first_name, student.last_name, student.gpa,
                             student.graduation_date, student.disciplinary_action])


# function to write major list (data property) to a file
def write_major_lists(students, filename_template):
    major_students = {}
    for student in students:
        # condition for student's major and appended to list.
        if student.major not in major_students:
            major_students[student.major] = []
        major_students[student.major].append(student)

    for major, students_list in major_students.items():
        #  assigning the filename and removing the space.
        filename = filename_template.format(major.replace(" ", ""))
        # writing sorted student's data properties to a file.
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Last Name", "First Name", "Graduation Date", "Disciplinary Action"])
            # sorting the students by student id.
            for student in sorted(students_list, key=sort_by_student_id):
                writer.writerow([student.student_id, student.last_name, student.first_name, student.graduation_date,
                                 student.disciplinary_action])

# function to check for graduated or not
def is_graduated(student):
    return (student.graduation_date is not None and
            datetime.strptime(student.graduation_date, "%m/%d/%Y") <= datetime.now())


# function to write student with scholarship eligibility to a file.
def write_scholarship_candidates(students, filename):
    scholarship_candidates = []
    for student in students:
        # condition for scholarship eligibility and appended to list.
        if (student.gpa is not None and student.gpa > 3.8 and not student.disciplinary_action
                and not is_graduated(student)):
            scholarship_candidates.append(student)
    # sorting the candidates by gpa from highest to lowest
    scholarship_candidates.sort(key=sort_by_gpa, reverse=True)
    # writing sorted student's data properties to a file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Last Name", "First Name", "Major", "GPA"])
        for student in scholarship_candidates:
            writer.writerow([student.student_id, student.last_name, student.first_name, student.major, student.gpa])


# function to write disciplined students data to a file
def write_disciplined_students(students, filename):
    disciplined_students = []
    for student in students:
        # condition to test if student disciplined is true.
        if student.disciplinary_action:
            disciplined_students.append(student)
    # sorting the students by graduation date
    disciplined_students.sort(key=sort_by_graduation_date)
    # writing sorted student's data properties to a file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Last Name", "First Name", "Graduation Date"])
        for student in disciplined_students:
            writer.writerow([student.student_id, student.last_name, student.first_name, student.graduation_date])


# calling all the defined functions above in "main" function.
def main():
    # assigning filenames from input.
    major_list = input("Enter the major list file name:")
    gpa_list = input("Enter the gpa list file name:")
    graduation_date_list = input("Enter the graduation date list file name:")

    # calling and assigning the data from the files to variables.
    students_data = read_csv(major_list)
    gpa_data = read_csv(gpa_list)
    graduation_data = read_csv(graduation_date_list)

    # Code with already named files for testing
    # students_data = read_csv("StudentsMajorsList.csv")
    # gpa_data = read_csv("GPAList.csv")
    # graduation_data = read_csv("GraduationDatesList.csv")

    # assigning all the datas read from the files to variable students by calling the process_students function.
    students = process_students(students_data, gpa_data, graduation_data)

    # calling all the write functions to write data to external files with the name mentioned in instruction.
    write_full_roster(students, "FullRoster.csv")
    write_major_lists(students, "{}Students.csv")
    write_scholarship_candidates(students, "ScholarshipCandidates.csv")
    write_disciplined_students(students, "DisciplinedStudents.csv")


# calling main function.
if __name__ == "__main__":
    main()
