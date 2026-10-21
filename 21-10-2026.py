import json
import os
from datetime import datetime

FILE_NAME = "sentiment_history.json"

POSITIVE_WORDS = {
    "happy", "good", "great", "excellent", "amazing",
    "love", "awesome", "wonderful", "best", "success",
    "beautiful", "fantastic", "enjoy", "helpful", "perfect"
}

NEGATIVE_WORDS = {
    "sad", "bad", "terrible", "awful", "hate",
    "worst", "angry", "boring", "fail", "failure",
    "poor", "horrible", "disappointed", "problem", "difficult"
}


def load_history():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_history(history):
    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)


def analyze_sentiment(text):
    words = text.lower().split()

    positive_count = sum(
        1 for word in words
        if word.strip(".,!?;:\"'()") in POSITIVE_WORDS
    )

    negative_count = sum(
        1 for word in words
        if word.strip(".,!?;:\"'()") in NEGATIVE_WORDS
    )

    if positive_count > negative_count:
        sentiment = "Positive"
    elif negative_count > positive_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, positive_count, negative_count


def analyze_text(history):
    text = input("\nEnter your text: ").strip()

    if not text:
        print("Text cannot be empty!")
        return

    sentiment, positive, negative = analyze_sentiment(text)

    result = {
        "text": text,
        "sentiment": sentiment,
        "positive_words": positive,
        "negative_words": negative,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    history.append(result)
    save_history(history)

    print("\n========== ANALYSIS ==========")
    print("Sentiment      :", sentiment)
    print("Positive words :", positive)
    print("Negative words :", negative)
    print("==============================")


def view_history(history):
    print("\n========== ANALYSIS HISTORY ==========")

    if not history:
        print("No analysis history found.")
        return

    for index, item in enumerate(history, start=1):
        print(f"\nAnalysis #{index}")
        print("Text      :", item["text"])
        print("Sentiment :", item["sentiment"])
        print("Date      :", item["date"])


def show_statistics(history):
    if not history:
        print("No statistics available yet.")
        return

    positive = sum(
        1 for item in history
        if item["sentiment"] == "Positive"
    )

    negative = sum(
        1 for item in history
        if item["sentiment"] == "Negative"
    )

    neutral = sum(
        1 for item in history
        if item["sentiment"] == "Neutral"
    )

    print("\n========== STATISTICS ==========")
    print("Total analyses :", len(history))
    print("Positive       :", positive)
    print("Negative       :", negative)
    print("Neutral        :", neutral)


def main():
    history = load_history()

    while True:
        print("\n===== TEXT SENTIMENT ANALYZER =====")
        print("1. Analyze Text")
        print("2. View History")
        print("3. View Statistics")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            analyze_text(history)
        elif choice == "2":
            view_history(history)
        elif choice == "3":
            show_statistics(history)
        elif choice == "4":
            print("Thanks for using Sentiment Analyzer!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
