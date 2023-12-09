# Name: Huzaifa Shoeb, ID: 1925670
# Final Project Part 2
import csv


# Define the functions and class


class Student:
    def __init__(self, student_id, last_name, first_name, major, disciplinary_action=False):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.major = major
        self.disciplinary_action = disciplinary_action


class GPARecord:
    def __init__(self, student_id, gpa):
        self.student_id = student_id
        self.gpa = gpa


class GraduationRecord:
    def __init__(self, student_id, graduation_date):
        self.student_id = student_id
        self.graduation_date = graduation_date


# function for reading the csv files


def read_csv(file_path, class_type):
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            records.append(class_type(*row))
    return records


# Some sort functions for the inputs as needed


def key_for_sorting(student):
    return float(student.gpa)


# Function to find the desired students
def find_students(major, gpa, students, gpas, graduations):
    valid_majors = set(student.major for student in students)

    if ',' in major or ',' in gpa:
        print("Invalid input: Major and GPA cannot contain commas.")
        return

    if major not in valid_majors:
        print("No such major")
        return

    if not gpa.replace('.', '', 1).isdigit():
        print("Invalid GPA format. Please enter a valid numeric GPA.")
        return

    gpa = float(gpa)

    # List to store the matching students data
    matching_students = []
    for student in students:
        if student.major == major and not student.disciplinary_action:
            matching_students.append(student)

    matching_students = [student for student in matching_students if student.student_id in
                         {gpa_record.student_id for gpa_record in gpas}]

    matching_students_within_range = [student for student in matching_students if
                                      abs(float(gpas_dict[student.student_id].gpa) - gpa) <= 0.1]
    matching_students_within_range.sort(key=key_for_sorting)

    # Find which students are in the desired matching range
    if matching_students_within_range:
        print("Your student(s):")
        for student in matching_students_within_range:
            print(f"{student.student_id}, {student.first_name} {student.last_name}, "
                  f"GPA: {gpas_dict[student.student_id].gpa}")
    else:
        matching_students_within_025_range = [student for student in matching_students if
                                              abs(float(gpas_dict[student.student_id].gpa) - gpa) <= 0.25]
        matching_students_within_025_range.sort(key=key_for_sorting)

        if matching_students_within_025_range:
            print("You may, also, consider:")
            for student in matching_students_within_025_range:
                print(f"{student.student_id}, {student.first_name} {student.last_name}, "
                      f"GPA: {gpas_dict[student.student_id].gpa}")
        else:
            closest_student = min(matching_students, key=key_for_sorting)
            print(f"The closest student in {major} is:")
            print(f"{closest_student.student_id}, {closest_student.first_name} {closest_student.last_name}, "
                  f"GPA: {gpas_dict[closest_student.student_id].gpa}")

    # Read the input files from the location in the computer


if __name__ == "__main__":
    students = read_csv("C:\\Users\\Huzaifa\\Desktop\\Project files\\StudentsMajorsList-3.csv", Student)
    gpas = read_csv("C:\\Users\\Huzaifa\\Desktop\\Project files\\GPAList-1.csv", GPARecord)
    graduations = read_csv("C:\\Users\\Huzaifa\\Desktop\\Project files\\GraduationDatesList-1.csv", GraduationRecord)

    gpas_dict = {gpa_record.student_id: gpa_record for gpa_record in gpas}
    graduations_dict = {graduation.student_id: graduation for graduation in graduations}

    while True:
        major = input("Enter major: ").strip()
        gpa = input("Enter GPA: ").strip()

        if major.lower() == 'q' or gpa.lower() == 'q':
            break

        find_students(major, gpa, students, gpas, graduations)
# Final Project Part 2 Code finished here
