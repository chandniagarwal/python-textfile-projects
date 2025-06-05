import datetime
import random

GOAL_STEPS = 8000
GOAL_WATER = 2.5
GOAL_SLEEP = 7

TIPS = [
    "💡 Stay hydrated by drinking a glass of water every 2 hours.",
    "💡 A 30-minute walk boosts your mood and heart health.",
    "💡 Aim to go to bed at the same time daily.",
    "💡 Deep breathing reduces stress and helps sleep.",
    "💡 Keep screen time low before bedtime for better sleep."
]

def add_health_data(file_path):
    date = datetime.date.today().isoformat()
    steps = input("Enter steps walked: ")
    water = input("Enter water intake in liters: ")
    sleep = input("Enter sleep hours: ")
    mood = input("How are you feeling today? (Happy, Tired, etc.): ")
    with open(file_path, "a") as f:
        f.write(f"{date}|{steps}|{water}|{sleep}|{mood}\n")
    print("Data added successfully!")
    print(random.choice(TIPS) + "\n")

def view_data_by_date(file_path):
    date = input("Enter date (YYYY-MM-DD) to view: ")
    with open(file_path, "r") as f:
        found = False
        for line in f:
            if line.startswith(date):
                print("Date | Steps | Water(L) | Sleep(Hrs) | Mood")
                print(line.strip())
                found = True
                break
        if not found:
            print("No data found for this date.\n")

def weekly_summary(file_path):
    from datetime import datetime, timedelta
    today = datetime.today()
    week_dates = [(today - timedelta(days=i)).date().isoformat() for i in range(7)]
    steps_total = water_total = sleep_total = count = 0
    best_day = {"steps": (0, ""), "water": (0, ""), "sleep": (0, "")}
    with open(file_path, "r") as f:
        next(f)  # skip header
        for line in f:
            date_str, steps, water, sleep, _ = line.strip().split("|")
            if date_str in week_dates:
                steps = int(steps)
                water = float(water)
                sleep = float(sleep)
                steps_total += steps
                water_total += water
                sleep_total += sleep
                count += 1
                if steps > best_day["steps"][0]:
                    best_day["steps"] = (steps, date_str)
                if water > best_day["water"][0]:
                    best_day["water"] = (water, date_str)
                if sleep > best_day["sleep"][0]:
                    best_day["sleep"] = (sleep, date_str)
    if count == 0:
        print("No data for the last 7 days.")
        return
    print("\n--- Weekly Summary ---")
    print(f"Days logged       : {count}")
    print(f"Average Steps     : {steps_total // count}")
    print(f"Average Water     : {round(water_total / count, 2)} L")
    print(f"Average Sleep     : {round(sleep_total / count, 2)} Hrs")
    print(f"Best Steps Day    : {best_day['steps'][1]} ({best_day['steps'][0]} steps)")
    print(f"Best Water Day    : {best_day['water'][1]} ({best_day['water'][0]} L)")
    print(f"Best Sleep Day    : {best_day['sleep'][1]} ({best_day['sleep'][0]} Hrs)")

    # Feedback
    if sleep_total / count < GOAL_SLEEP:
        print("🛌 Try to sleep at least 7 hours a day.")
    if water_total / count < GOAL_WATER:
        print("💧 Drink more water to stay hydrated.")
    if steps_total / count < GOAL_STEPS:
        print("🚶 Increase your activity to reach 8,000+ steps daily.")
    else:
        print("✅ Great job! You're consistent!")
    print("--------------------------\n")

def main():
    file_path = "health_log_enhanced.txt"
    while True:
        print("\n--- Health Tracker Menu ---")
        print("1. Add today's health data")
        print("2. View data for a date")
        print("3. View last 7 days summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_health_data(file_path)
        elif choice == '2':
            view_data_by_date(file_path)
        elif choice == '3':
            weekly_summary(file_path)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
