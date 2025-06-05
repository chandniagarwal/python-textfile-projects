import csv

def read_student_data():
    try:
        with open('student_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            
            return list(reader)
    except FileNotFoundError:
        print("student_data.csv file not found.")
        return []
def read_student_data_formatted():
    try:
        with open('student_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            print("\n{:<10} {:<15} {:<8} {:<8} {:<10}".format('Roll No', 'Name', 'Maths', 'Science', 'Computer'))
            print("-" * 55)
            for student in data:
                print("{:<10} {:<15} {:<8} {:<8} {:<10}".format(
                    student['Roll No'],
                    student['Name'],
                    student['Maths'],
                    student['Science'],
                    student['Computer']
                ))
            print()

            return data
    except FileNotFoundError:
        print("student_data.csv file not found.")
        return []



def search_student(roll_number, data):
    for student in data:
        if student['Roll No'] == roll_number:
            return student
    return None

def calculate_grade(marks):
    marks = int(marks)
    if marks >= 90:
        return 'A+'
    elif marks >= 75:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'

def generate_report(student):
    report = f"Report Card for Roll No: {student['Roll No']}\n"
    report += f"Name: {student['Name']}\n"
    report += f"Maths: {student['Maths']} - Grade: {calculate_grade(student['Maths'])}\n"
    report += f"Science: {student['Science']} - Grade: {calculate_grade(student['Science'])}\n"
    report += f"Computer: {student['Computer']} - Grade: {calculate_grade(student['Computer'])}\n"
    report += f"Total: {int(student['Maths']) + int(student['Science']) + int(student['Computer'])}\n"
    return report

def save_report_to_file(roll_number, report):
    with open(f"ReportCard_{roll_number}.txt", "w") as file:
        file.write(report)

def add_new_student():
    print("\nEnter details for the new student:")
    roll_no = input("Roll No: ")
    name = input("Name: ")
    maths = input("Maths Marks: ")
    science = input("Science Marks: ")
    computer = input("Computer Marks: ")

    with open('student_data.csv', 'a', newline='') as file:
        fieldnames = ['Roll No', 'Name', 'Maths', 'Science', 'Computer']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'Roll No': roll_no,
            'Name': name,
            'Maths': maths,
            'Science': science,
            'Computer': computer
        })
    print("New student record added successfully.\n")

def main():
    while True:
        print("\n--- Student Report Card Generator ---")
        print("1. View All Student Records")
        print("2. View All Student Records in formatted way")
        print("3. Search and Generate Report Card")
        print("4. Export Report to File")
        print("5. Add New Student Record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = read_student_data()
            for student in data:
                print(student)
        elif choice == '2':
            data = read_student_data_formatted()
              
        elif choice == '2':
            roll = input("Enter Roll No: ")
            data = read_student_data()
            student = search_student(roll, data)
            if student:
                print(generate_report(student))
            else:
                print("Student not found.")
        elif choice == '3':
            roll = input("Enter Roll No: ")
            data = read_student_data()
            student = search_student(roll, data)
            if student:
                report = generate_report(student)
                save_report_to_file(roll, report)
                print(f"Report saved to ReportCard_{roll}.txt")
            else:
                print("Student not found.")
        elif choice == '4':
            add_new_student()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
main()
