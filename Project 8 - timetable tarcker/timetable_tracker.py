import csv

FILE_NAME = "timetable.csv"

def load_timetable():
    with open(FILE_NAME, newline='') as file:
        reader = list(csv.reader(file))
        return reader

def save_timetable(data):
    with open(FILE_NAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def view_timetable(data):
    print("\n--- Weekly Time Table ---")
    for row in data:
        print(" | ".join(row))
    print()

def assign_subject(data):
    day = input("Enter day (e.g., Monday): ").capitalize()
    period = input("Enter period number (1-5): ")
    subject = input("Enter subject name: ")

    # Find day row
    for i in range(1, len(data)):
        if data[i][0].lower() == day.lower():
            period_index = int(period)
            if data[i][period_index] == "---":
                data[i][period_index] = subject
                print("Subject assigned successfully!\n")
                return True
            else:
                print("Slot already occupied!\n")
                return False
    print("Invalid day entered.\n")
    return False

def export_timetable_txt(data):
    with open("timetable_export.txt", "w") as file:
        for row in data:
            file.write(" | ".join(row) + "\n")
    print("Timetable exported to 'timetable_export.txt'\n")

def main():
    data = load_timetable()
    while True:
        print("--- Time Table Tracker ---")
        print("1. View Time Table")
        print("2. Assign Subject to Slot")
        print("3. Export Time Table to TXT")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_timetable(data)
        elif choice == '2':
            if assign_subject(data):
                save_timetable(data)
        elif choice == '3':
            export_timetable_txt(data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
