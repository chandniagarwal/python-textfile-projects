import datetime
import os

DIARY_FILE = "diary.txt"
PASSWORD = "mydiary2025"

def check_password():
    attempt = input("Enter password to access your diary: ")
    if attempt == PASSWORD:
        print("Access granted.\n")
        return True
    else:
        print("Incorrect password. Access denied.\n")
        return False

def write_entry():
    entry = input("Write your diary entry: ")
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M]")
    with open(DIARY_FILE, "a") as f:
        f.write(f"{timestamp}\n{entry}\n\n")
    print("Entry saved successfully!\n")

def view_entries_by_date():
    date = input("Enter date to search (YYYY-MM-DD): ")
    with open(DIARY_FILE, "r") as f:
        lines = f.readlines()
    found = False
    print(f"\n--- Entries for {date} ---")
    for i in range(len(lines)):
        if lines[i].startswith(f"[{date}"):
            found = True
            print(lines[i], end='')
            j = i + 1
            while j < len(lines) and not lines[j].startswith('['):
                print(lines[j], end='')
                j += 1
            print("-" * 30)
    if not found:
        print("No entries found for this date.\n")

def export_entry():
    date = input("Enter date to export (YYYY-MM-DD): ")
    with open(DIARY_FILE, "r") as f:
        lines = f.readlines()
    found = False
    content = ""
    for i in range(len(lines)):
        if lines[i].startswith(f"[{date}"):
            found = True
            content += lines[i]
            j = i + 1
            while j < len(lines) and not lines[j].startswith('['):
                content += lines[j]
                j += 1
    if found:
        filename = f"Diary_{date}.txt"
        with open(filename, "w") as f:
            f.write(content)
        print(f"Entry exported to {filename}\n")
    else:
        print("No entries found for that date.\n")

def main():
    if not check_password():
        return

    while True:
        print("--- Diary Menu ---")
        print("1. Write a new entry")
        print("2. View entries by date")
        print("3. Export entry to file")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            write_entry()
        elif choice == '2':
            view_entries_by_date()
        elif choice == '3':
            export_entry()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
