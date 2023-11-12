# Name: Huzaifa Shoeb, ID: 1925670
# Final Project Part 1
import csv


# Define the functions and class
class Student:
    def __init__(self, student_id, last_name, first_name, major, disciplinary_action=False):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.disciplinary_action = disciplinary_action
        self.gpa = None
        self.graduation_date = None

    def set_gpa(self, gpa):
        self.gpa = gpa

    def set_graduation_date(self, graduation_date):
        self.graduation_date = graduation_date


# function for reading the csv files
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


# function for writing in the csv files
def write_csv(file_path, header, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)


# Some sort functions for the inputs as needed
def sort_by_last_name(student):
    return student[3]


def sort_by_graduation_date(student):
    return student[3]


def sort_by_student_id(student):
    return student[0]


def sort_by_gpa(student):
    return student[4]


# The main function that wil generate the desired results for the reports
def processed_inventory_reports():
    # Read the input files from the location in the computer
    student_data = read_csv("C:\\Users\\Huzaifa\\Desktop\\Project files\\StudentsMajorsList.csv")
    gpa_list = read_csv("C:\\Users\\Huzaifa\\Desktop\\Project files\\GPAList.csv")
    graduation_dates_list = read_csv("C:\\Users\\Huzaifa\\Desktop\\Project files\\GraduationDatesList.csv")

    # Creating a dictionary for student information
    students = {}
    for student_row in student_data:
        student_id, last_name, first_name, major, disciplinary_action = student_row
        student = Student(student_id, last_name, first_name, major, disciplinary_action)
        students[student_id] = student

    # Set the GPA
    for gpa_row in gpa_list:
        student_id, gpa = gpa_row
        # Convert student_id to string
        student_id = str(student_id)

        # Check if the student id is in the dictionary
        if student_id in students:
            students[student_id].set_gpa(float(gpa))


# Set graduation dates for the students
    for _ in graduation_dates_list:
        pass

    # Give output
    full_roster = []
    computer_information_systems_students = {}
    scholarship_candidates = []
    disciplined_students = []

    for student in students.values():
        full_roster.append([student.student_id, student.major, student.first_name, student.last_name,
                           student.gpa, student.graduation_date, student.disciplinary_action])

        if student.major not in computer_information_systems_students:
            computer_information_systems_students[student.major] = []

        computer_information_systems_students[student.major].append(
            [student.student_id, student.last_name, student.first_name, student.graduation_date,
             student.disciplinary_action])

        if student.gpa > 3.8 and not student.disciplinary_action and not student.graduation_date:
            scholarship_candidates.append(
                [student.student_id, student.last_name, student.first_name, student.major, student.gpa])

        if student.disciplinary_action:
            disciplined_students.append([student.student_id, student.last_name, student.first_name,
                                         student.graduation_date])

    # Sort by last name
    full_roster.sort(key=sort_by_last_name)

    def sort_by_graduation(student_use):
        # Use the infinite value as assignment so that the none values do not affect the code
        return student_use[3] if student_use[3] is not None else float('inf')

    # Part a requirements for project
    full_roster.sort(key=sort_by_last_name, reverse=False)
    write_csv('FullRoster.csv', ['Student ID', 'Major', 'First Name', 'Last Name', 'GPA', 'Graduation Date',
                                 'Disciplinary Action'], full_roster)

    # Part b requirements for project
    for major, students_list in computer_information_systems_students.items():
        students_list.sort(key=sort_by_student_id)  # Sort by student ID
        write_csv(f"{major.replace(' ', '')}Students.csv", ['Student ID', 'Last Name', 'First Name', 'Graduation Date',
                                                            'Disciplinary Action'], students_list)

    # Part c requirements for project
    scholarship_candidates.sort(key=sort_by_gpa, reverse=True)  # Sort by GPA
    write_csv('ScholarshipCandidates.csv', ['Student ID', 'Last Name', 'First Name', 'Major', 'GPA'],
              scholarship_candidates)

    # Part d requirements for project
    disciplined_students.sort(key=sort_by_graduation, reverse=True)  # Sort by graduation date
    write_csv('DisciplinedStudents.csv', ['Student ID', 'Last Name', 'First Name', 'Graduation Date'],
              disciplined_students)


if __name__ == '__main__':
    processed_inventory_reports()
# Final Project Part 1 Code finished here
