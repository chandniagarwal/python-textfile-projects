import csv

def load_students(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        return [row[0] for row in reader]

def generate_seating_chart(students, room_capacity=4):
    rooms = []
    room_number = 1
    i = 0
    while i < len(students):
        room = []
        for seat in range(room_capacity):
            if i < len(students):
                room.append(students[i])
                i += 1
        rooms.append((f"Room {room_number}", room))
        room_number += 1
    return rooms

def save_seating_chart(rooms, filename="seating.txt"):
    with open(filename, "w") as f:
        for room_name, students in rooms:
            f.write(f"{room_name}:\n")
            for i, roll in enumerate(students, 1):
                f.write(f"  Seat {i} - Roll No: {roll}\n")
            f.write("\n")
    print(f"Seating chart saved to {filename}\n")

def main():
    students = load_students("students.csv")
    rooms = generate_seating_chart(students, room_capacity=4)
    save_seating_chart(rooms)

if __name__ == "__main__":
    main()
