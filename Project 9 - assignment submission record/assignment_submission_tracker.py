import csv

FILENAME = "submissions.csv"

def load_data():
    with open(FILENAME, newline='') as file:
        reader = list(csv.reader(file))
        return reader

def save_data(data):
    with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def view_all(data):
    print("\n--- All Submissions ---")
    for row in data:
        print(" | ".join(row))
    print()

def update_submission(data):
    roll = input("Enter roll number to update: ")
    for i in range(1, len(data)):
        if data[i][0] == roll:
            status = input("Enter status (Yes/No): ").capitalize()
            data[i][2] = "Yes" if status == "Yes" else "No"
            print("Submission status updated.\n")
            return True
    print("Roll number not found.\n")
    return False

def view_defaulters(data):
    print("\n--- Defaulter List ---")
    found = False
    for row in data[1:]:
        if row[2].lower() == "no":
            print(f"{row[0]} - {row[1]}")
            found = True
    if not found:
        print("No defaulters found.")
    print()

def export_defaulters(data):
    with open("defaulters.txt", "w") as f:
        f.write("Defaulter List\n----------------\n")
        for row in data[1:]:
            if row[2].lower() == "no":
                f.write(f"{row[0]} - {row[1]}\n")
    print("Defaulter list exported to defaulters.txt\n")

def main():
    data = load_data()
    while True:
        print("--- Assignment Submission Tracker ---")
        print("1. View All Submissions")
        print("2. Update Submission Status")
        print("3. View Defaulters")
        print("4. Export Defaulter List")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_all(data)
        elif choice == '2':
            if update_submission(data):
                save_data(data)
        elif choice == '3':
            view_defaulters(data)
        elif choice == '4':
            export_defaulters(data)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
