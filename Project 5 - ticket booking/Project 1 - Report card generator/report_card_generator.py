import csv

# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

# Function to read student data from CSV file
def read_student_data(filename):
    students = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = {
                'Roll No': int(row['Roll No']),
                'Name': row['Name'],
                'Class': row['Class'],
                'Math': int(row['Math']),
                'Physics': int(row['Physics']),
                'CS': int(row['CS'])
            }
            total = student['Math'] + student['Physics'] + student['CS']
            percentage = round(total / 3, 2)
            grade = calculate_grade(percentage)
            student['Total'] = total
            student['Percentage'] = percentage
            student['Grade'] = grade
            students.append(student)
    return students

# Function to display formatted report card
def display_report_card(student):
    print("\n----- Report Card -----")
    print(f"Roll No   : {student['Roll No']}")
    print(f"Name      : {student['Name']}")
    print(f"Class     : {student['Class']}")
    print(f"Math      : {student['Math']}")
    print(f"Physics   : {student['Physics']}")
    print(f"CS        : {student['CS']}")
    print(f"Total     : {student['Total']}")
    print(f"Percentage: {student['Percentage']}%")
    print(f"Grade     : {student['Grade']}")
    print("------------------------\n")

# Function to save report card to a text file
def save_report_card(student):
    filename = f"ReportCard_{student['Roll No']}.txt"
    with open(filename, mode='w') as file:
        file.write("----- Report Card -----\n")
        file.write(f"Roll No   : {student['Roll No']}\n")
        file.write(f"Name      : {student['Name']}\n")
        file.write(f"Class     : {student['Class']}\n")
        file.write(f"Math      : {student['Math']}\n")
        file.write(f"Physics   : {student['Physics']}\n")
        file.write(f"CS        : {student['CS']}\n")
        file.write(f"Total     : {student['Total']}\n")
        file.write(f"Percentage: {student['Percentage']}%\n")
        file.write(f"Grade     : {student['Grade']}\n")
        file.write("------------------------\n")
    print(f"Report card saved to {filename}\n")

# Menu-driven program
def main():
    filename = 'student_data.csv'
    students = read_student_data(filename)

    while True:
        print("\n--- Student Report Card Menu ---")
        print("1. Display all report cards")
        print("2. Search by roll number")
        print("3. Save a report card to file")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            for student in students:
                display_report_card(student)
        elif choice == '2':
            roll = int(input("Enter roll number to search: "))
            found = False
            for student in students:
                if student['Roll No'] == roll:
                    display_report_card(student)
                    found = True
                    break
            if not found:
                print("Student not found!")
        elif choice == '3':
            roll = int(input("Enter roll number to save report card: "))
            found = False
            for student in students:
                if student['Roll No'] == roll:
                    save_report_card(student)
                    found = True
                    break
            if not found:
                print("Student not found!")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

main()
