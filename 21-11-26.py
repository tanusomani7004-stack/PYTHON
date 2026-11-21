
import time
import random

sentences = [
    "Python is a powerful programming language",
    "Practice makes a programmer perfect",
    "Data structures help organize information",
    "Learning new skills creates opportunities",
    "Consistency is the key to success",
    "Artificial intelligence is changing the world",
    "Coding improves logical thinking and creativity"
]


def calculate_accuracy(original, typed):
    correct = 0

    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1

    if len(original) == 0:
        return 0

    accuracy = (correct / len(original)) * 100
    return round(accuracy, 2)


def calculate_wpm(typed_text, elapsed_time):
    words = len(typed_text.split())

    minutes = elapsed_time / 60

    if minutes == 0:
        return 0

    return round(words / minutes, 2)


def start_test():
    sentence = random.choice(sentences)

    print("\nType the following sentence:")
    print("\n", sentence)

    input("\nPress Enter when you are ready...")

    print("\nStart typing now!")
    start_time = time.time()

    typed_text = input("\nYour Text: ")

    end_time = time.time()

    elapsed_time = end_time - start_time

    wpm = calculate_wpm(typed_text, elapsed_time)
    accuracy = calculate_accuracy(sentence, typed_text)

    correct = 0

    for i in range(min(len(sentence), len(typed_text))):
        if sentence[i] == typed_text[i]:
            correct += 1

    incorrect = max(len(sentence), len(typed_text)) - correct

    print("\n========== TEST RESULT ==========")
    print("Time Taken:", round(elapsed_time, 2), "seconds")
    print("Typing Speed:", wpm, "WPM")
    print("Accuracy:", accuracy, "%")
    print("Correct Characters:", correct)
    print("Incorrect Characters:", incorrect)

    return wpm, accuracy


def main():
    results = []

    while True:
        print("\n======= TYPING SPEED TESTER =======")
        print("1. Start Test")
        print("2. View Performance")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            wpm, accuracy = start_test()

            results.append({
                "wpm": wpm,
                "accuracy": accuracy
            })

        elif choice == "2":
            if not results:
                print("No test results available!")
                continue

            print("\n========== PERFORMANCE ==========")

            for i, result in enumerate(results, start=1):
                print(
                    f"Round {i}: "
                    f"{result['wpm']} WPM | "
                    f"{result['accuracy']}% Accuracy"
                )

            average_wpm = sum(
                result["wpm"] for result in results
            ) / len(results)

            average_accuracy = sum(
                result["accuracy"] for result in results
            ) / len(results)

            print("\nAverage WPM:", round(average_wpm, 2))
            print("Average Accuracy:", round(average_accuracy, 2))

        elif choice == "3":
            print("Thanks for using Typing Speed Tester!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
