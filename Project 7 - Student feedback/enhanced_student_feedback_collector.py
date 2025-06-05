import datetime

FEEDBACK_FILE = "feedback_enhanced.txt"

positive_keywords = ["good", "great", "well", "excellent", "amazing", "helpful", "nice"]
negative_keywords = ["bad", "not", "poor", "problem", "slow", "broken", "issue"]

def detect_sentiment(comment):
    text = comment.lower()
    if any(word in text for word in positive_keywords):
        return "Positive"
    elif any(word in text for word in negative_keywords):
        return "Negative"
    else:
        return "Neutral"

def submit_feedback():
    print("\n--- Submit Feedback ---")
    category = input("Enter category (Teaching / Facilities / Labs / Suggestions): ").strip().capitalize()
    name = input("Enter your name (or press Enter to remain anonymous): ").strip()
    if name == "":
        name = "Anonymous"
    comment = input("Enter your feedback: ").strip()
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M]")
    sentiment = detect_sentiment(comment)
    with open(FEEDBACK_FILE, "a") as f:
        f.write(f"{timestamp} | {category} | {comment} | Submitted by: {name} | Sentiment: {sentiment}\n")
    print("Thank you! Your feedback has been recorded.\n")

def view_feedback_by_category():
    cat = input("Enter category to view: ").strip().capitalize()
    print(f"\n--- Feedback for {cat} ---")
    found = False
    with open(FEEDBACK_FILE, "r") as f:
        for line in f:
            if f"| {cat} |" in line:
                print(line.strip())
                found = True
    if not found:
        print("No feedback found in this category.\n")

def view_feedback_by_sentiment(sentiment):
    print(f"\n--- {sentiment} Feedback ---")
    found = False
    with open(FEEDBACK_FILE, "r") as f:
        for line in f:
            if f"Sentiment: {sentiment}" in line:
                print(line.strip())
                found = True
    if not found:
        print(f"No {sentiment.lower()} feedback found.\n")

def view_all_feedback():
    print("\n--- All Feedback ---")
    with open(FEEDBACK_FILE, "r") as f:
        print(f.read())

def delete_feedback():
    keyword = input("Enter part of the comment or category to delete: ").strip()
    with open(FEEDBACK_FILE, "r") as f:
        lines = f.readlines()
    new_lines = [line for line in lines if keyword.lower() not in line.lower()]
    with open(FEEDBACK_FILE, "w") as f:
        f.writelines(new_lines)
    print("Matching feedback deleted (if any).\n")

def export_feedback_by_category():
    category = input("Enter category to export: ").strip().capitalize()
    filename = f"{category.lower()}_feedback.txt"
    with open(FEEDBACK_FILE, "r") as f:
        lines = [line for line in f if f"| {category} |" in line]
    if lines:
        with open(filename, "w") as f:
            f.writelines(lines)
        print(f"Feedback exported to {filename}\n")
    else:
        print("No feedback found in this category.\n")

def main():
    while True:
        print("\n--- Enhanced Student Feedback Collector ---")
        print("1. Submit Feedback")
        print("2. View Feedback by Category")
        print("3. View All Feedback")
        print("4. Delete Feedback")
        print("5. View Positive Feedback")
        print("6. View Negative Feedback")
        print("7. Export Feedback by Category")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            submit_feedback()
        elif choice == '2':
            view_feedback_by_category()
        elif choice == '3':
            view_all_feedback()
        elif choice == '4':
            delete_feedback()
        elif choice == '5':
            view_feedback_by_sentiment("Positive")
        elif choice == '6':
            view_feedback_by_sentiment("Negative")
        elif choice == '7':
            export_feedback_by_category()
        elif choice == '8':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
