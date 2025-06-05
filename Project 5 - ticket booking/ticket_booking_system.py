def load_tickets(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    header = lines[0].strip()
    records = [line.strip().split("|") for line in lines[1:]]
    return header, records

def save_tickets(filename, header, records):
    with open(filename, "w") as file:
        file.write(header + "\n")
        for record in records:
            file.write("|".join(record) + "\n")

def show_available_tickets(records):
    print("\n--- Available Tickets ---")
    for r in records:
        if r[3] == "Available":
            print(f"{r[0]} - {r[2]} ({r[3]})")
    print()

def view_all_bookings(records):
    print("\n--- All Bookings ---")
    for r in records:
        name_display = r[1] if r[1] != "---" else "None"
        print(f"{r[0]} - {r[2]} - {name_display} ({r[3]})")
    print()

def book_ticket(records):
    name = input("Enter your name: ")
    for r in records:
        if r[3] == "Available":
            r[1] = name
            r[3] = "Booked"
            print(f"Ticket {r[0]} booked successfully for {name}!")
            with open(f"Ticket_{r[0]}.txt", "w") as f:
                f.write(f"Ticket ID: {r[0]}\nName: {name}\nEvent: {r[2]}\nStatus: Booked")
            return True
    print("No tickets available.")
    return False

def cancel_booking(records):
    ticket_id = input("Enter Ticket ID to cancel: ").upper()
    for r in records:
        if r[0] == ticket_id and r[3] == "Booked":
            r[1] = "---"
            r[3] = "Available"
            print(f"Ticket {ticket_id} has been cancelled.")
            return True
    print("Ticket not found or not booked.")
    return False

def main():
    filename = "tickets.txt"
    header, records = load_tickets(filename)

    while True:
        print("--- E-Ticket Booking System ---")
        print("1. Show Available Tickets")
        print("2. Book a Ticket")
        print("3. Cancel Booking")
        print("4. View All Bookings")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_available_tickets(records)
        elif choice == '2':
            if book_ticket(records):
                save_tickets(filename, header, records)
        elif choice == '3':
            if cancel_booking(records):
                save_tickets(filename, header, records)
        elif choice == '4':
            view_all_bookings(records)
        elif choice == '5':
            print("Thank you for using the E-Ticket Booking System.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
