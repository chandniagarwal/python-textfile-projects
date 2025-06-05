positive_keywords = ["good", "great", "well", "interactive", "fun", "helpful", "excellent", "nice"]
negative_keywords = ["bad", "not", "poor", "didn't", "boring", "dislike", "hate", "slow", "late"]

def detect_sentiment(comment):
    comment = comment.lower()
    if any(word in comment for word in positive_keywords):
        return "Positive"
    elif any(word in comment for word in negative_keywords):
        return "Negative"
    else:
        return "Neutral"

def classify_comments():
    with open("comments.txt", "r") as f:
        comments = f.readlines()

    classified = {"Positive": [], "Negative": [], "Neutral": []}
    for line in comments:
        sentiment = detect_sentiment(line)
        classified[sentiment].append(line.strip())

    return classified

def view_all_comments():
    print("\n--- All Comments ---")
    with open("comments.txt", "r") as f:
        for line in f:
            print(line.strip())
    print()

def view_comments_by_sentiment(classified):
    sentiment = input("Enter sentiment to view (Positive/Negative/Neutral): ").capitalize()
    if sentiment in classified:
        print(f"\n--- {sentiment} Comments ---")
        for comment in classified[sentiment]:
            print(comment)
        print()
    else:
        print("Invalid sentiment.\n")

def export_classified_comments(classified):
    for category, comments in classified.items():
        with open(f"{category.lower()}_comments.txt", "w") as f:
            for comment in comments:
                f.write(comment + "\n")
    print("Classified comments exported as separate files.\n")

def count_sentiments(classified):
    print("\n--- Sentiment Summary ---")
    for k, v in classified.items():
        print(f"{k} Comments: {len(v)}")
    print()

def main():
    while True:
        print("--- Student Comment Analyzer ---")
        print("1. View All Comments")
        print("2. View Comments by Sentiment")
        print("3. Export Comments to Files")
        print("4. Count Comments by Sentiment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_all_comments()
        elif choice == '2':
            classified = classify_comments()
            view_comments_by_sentiment(classified)
        elif choice == '3':
            classified = classify_comments()
            export_classified_comments(classified)
        elif choice == '4':
            classified = classify_comments()
            count_sentiments(classified)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
