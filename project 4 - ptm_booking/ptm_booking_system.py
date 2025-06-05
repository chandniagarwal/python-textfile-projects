import csv

def load_slots(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        slots = [row for row in reader]
    return header, slots

def save_slots(filename, header, slots):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(slots)

def show_available_slots(slots):
    print("\n--- Available Slots ---")
    for slot in slots:
        if slot[3] == "Available":
            print(f"{slot[0]} | {slot[1]} ({slot[3]})")
    print()

def book_slot(slots):
    show_available_slots(slots)
    slot_id = input("Enter Slot ID to book: ").upper()
    name = input("Enter Parent Name: ")
    for slot in slots:
        if slot[0] == slot_id and slot[3] == "Available":
            slot[2] = name
            slot[3] = "Booked"
            with open(f"Confirmation_{slot_id}.txt", "w") as f:
                f.write(f"Confirmation Receipt\n---------------------\n")
                f.write(f"Slot ID  : {slot[0]}\nTime     : {slot[1]}\nParent   : {name}\nStatus   : Booked\n")
            print(f"Slot {slot_id} booked successfully! Confirmation file generated.\n")
            return True
    print("Invalid Slot ID or already booked.\n")
    return False

def view_all_bookings(slots):
    print("\n--- All Bookings ---")
    for slot in slots:
        print(f"{slot[0]} | {slot[1]} | {slot[2]} | {slot[3]}")
    print()

def main():
    filename = "ptm_slots.csv"
    header, slots = load_slots(filename)

    while True:
        print("--- PTM Slot Booking System ---")
        print("1. View Available Slots")
        print("2. Book a Slot")
        print("3. View All Bookings")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_available_slots(slots)
        elif choice == '2':
            if book_slot(slots):
                save_slots(filename, header, slots)
        elif choice == '3':
            view_all_bookings(slots)
        elif choice == '4':
            print("Thank you for using the PTM Booking System.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
