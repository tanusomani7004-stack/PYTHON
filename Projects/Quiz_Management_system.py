import random

questions = [
    {
        "question": "Which language is mainly used for AI and ML?",
        "options": ["Java", "Python", "HTML", "CSS"],
        "answer": "Python"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
        "answer": "O(log n)"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "define", "def", "func"],
        "answer": "def"
    },
    {
        "question": "Which library is commonly used for data analysis?",
        "options": ["Pandas", "React", "Express", "Bootstrap"],
        "answer": "Pandas"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "/*", "#", "<!--"],
        "answer": "#"
    },
    {
        "question": "Which collection does NOT allow duplicate values?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "answer": "Set"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing Unit"
        ],
        "answer": "Central Processing Unit"
    }
]


def show_question(question, number):
    print("\n" + "=" * 50)
    print(f"Question {number}")
    print("=" * 50)

    print(question["question"])

    for index, option in enumerate(question["options"], start=1):
        print(f"{index}. {option}")


def get_answer():
    while True:
        try:
            choice = int(input("\nEnter your answer (1-4): "))

            if 1 <= choice <= 4:
                return choice

            print("❌ Choose between 1 and 4.")

        except ValueError:
            print("❌ Please enter a number.")


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def start_quiz():
    quiz_questions = questions.copy()

    random.shuffle(quiz_questions)

    # Take 5 random questions
    quiz_questions = quiz_questions[:5]

    score = 0
    wrong_answers = []

    for number, question in enumerate(quiz_questions, start=1):

        show_question(question, number)

        choice = get_answer()

        selected_answer = question["options"][choice - 1]

        if selected_answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")
            print("Correct answer:", question["answer"])

            wrong_answers.append({
                "question": question["question"],
                "your_answer": selected_answer,
                "correct_answer": question["answer"]
            })

    show_result(score, len(quiz_questions), wrong_answers)


def show_result(score, total, wrong_answers):

    percentage = (score / total) * 100
    grade = calculate_grade(percentage)

    print("\n")
    print("╔" + "═" * 48 + "╗")
    print("║" + "           🎯 QUIZ RESULT           " + "║")
    print("╚" + "═" * 48 + "╝")

    print(f"\nScore      : {score}/{total}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")

    if percentage >= 80:
        print("🏆 Excellent performance!")
    elif percentage >= 60:
        print("👍 Good job!")
    else:
        print("📚 Keep practicing!")

    if wrong_answers:

        print("\n========== WRONG ANSWERS ==========")

        for item in wrong_answers:
            print(f"\nQuestion: {item['question']}")
            print(f"Your answer: {item['your_answer']}")
            print(f"Correct answer: {item['correct_answer']}")


def main():

    print("\n========================================")
    print("        🧠 PYTHON QUIZ SYSTEM")
    print("========================================")

    while True:

        start_quiz()

        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("\n👋 Thanks for playing!")
            break


main()
