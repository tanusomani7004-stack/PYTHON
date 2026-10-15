import json
import os
import random
from datetime import datetime

QUESTIONS_FILE = "questions.json"
RESULTS_FILE = "results.json"

DEFAULT_QUESTIONS = [
    {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": 2,
        "topic": "Data Structures"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": 3,
        "topic": "Python"
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
        "answer": 2,
        "topic": "Algorithms"
    },
    {
        "question": "Which SQL command retrieves data?",
        "options": ["GET", "OPEN", "SELECT", "FETCH ALL"],
        "answer": 3,
        "topic": "DBMS"
    },
    {
        "question": "Which library is commonly used for data analysis?",
        "options": ["Pandas", "Turtle", "Pygame", "Tkinter"],
        "answer": 1,
        "topic": "Data Science"
    }
]


def load_json(filename, default):
    if not os.path.exists(filename):
        return default

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print(f"Warning: Could not read {filename}.")
        return default


def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def get_grade(percentage):
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Very Good"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 40:
        return "Needs Practice"
    else:
        return "Keep Learning"


def start_quiz(questions, results):
    if not questions:
        print("No questions available.")
        return

    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    score = 0
    topic_stats = {}

    print("\n========== QUIZ STARTED ==========")

    for number, question in enumerate(quiz_questions, start=1):
        print(f"\nQ{number}. {question['question']}")

        for index, option in enumerate(question["options"], start=1):
            print(f"{index}. {option}")

        try:
            answer = int(input("Your answer (1-4): "))
        except ValueError:
            answer = 0

        topic = question["topic"]

        if topic not in topic_stats:
            topic_stats[topic] = {"correct": 0, "total": 0}

        topic_stats[topic]["total"] += 1

        if answer == question["answer"]:
            print("Correct!")
            score += 1
            topic_stats[topic]["correct"] += 1
        else:
            correct_option = question["options"][
                question["answer"] - 1
            ]
            print("Incorrect. Correct answer:", correct_option)

    percentage = score / len(quiz_questions) * 100

    result = {
        "name": name,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "score": score,
        "total": len(quiz_questions),
        "percentage": round(percentage, 2),
        "grade": get_grade(percentage),
        "topics": topic_stats
    }

    results.append(result)
    save_json(RESULTS_FILE, results)

    print("\n========== YOUR RESULT ==========")
    print("Student:", name)
    print(f"Score: {score}/{len(quiz_questions)}")
    print(f"Percentage: {percentage:.2f}%")
    print("Performance:", result["grade"])

    print("\nTopic-wise performance:")

    for topic, stats in topic_stats.items():
        print(
            f"{topic}: {stats['correct']}/{stats['total']} correct"
        )


def view_results(results):
    print("\n========== PREVIOUS RESULTS ==========")

    if not results:
        print("No results available.")
        return

    for result in results:
        print(
            f"{result['name']} | "
            f"{result['score']}/{result['total']} | "
            f"{result['percentage']}% | "
            f"{result['grade']} | "
            f"{result['date']}"
        )


def show_leaderboard(results):
    if not results:
        print("No quiz results available.")
        return

    leaderboard = sorted(
        results,
        key=lambda result: result["percentage"],
        reverse=True
    )

    print("\n========== LEADERBOARD ==========")

    for rank, result in enumerate(leaderboard[:10], start=1):
        print(
            f"{rank}. {result['name']} - "
            f"{result['percentage']}%"
        )


def show_topic_analysis(results):
    topic_totals = {}

    for result in results:
        for topic, stats in result.get("topics", {}).items():
            if topic not in topic_totals:
                topic_totals[topic] = {"correct": 0, "total": 0}

            topic_totals[topic]["correct"] += stats["correct"]
            topic_totals[topic]["total"] += stats["total"]

    if not topic_totals:
        print("No topic performance data available.")
        return

    print("\n========== TOPIC ANALYSIS ==========")

    for topic, stats in topic_totals.items():
        accuracy = stats["correct"] / stats["total"] * 100

        print(
            f"{topic}: {accuracy:.1f}% accuracy "
            f"({stats['correct']}/{stats['total']})"
        )


def main():
    questions = load_json(QUESTIONS_FILE, DEFAULT_QUESTIONS)
    results = load_json(RESULTS_FILE, [])

    while True:
        print("\n===== QUIZ PERFORMANCE ANALYZER =====")
        print("1. Start Quiz")
        print("2. View Previous Results")
        print("3. View Leaderboard")
        print("4. Analyze Topic Performance")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_quiz(questions, results)
        elif choice == "2":
            view_results(results)
        elif choice == "3":
            show_leaderboard(results)
        elif choice == "4":
            show_topic_analysis(results)
        elif choice == "5":
            print("Keep learning and improving!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
