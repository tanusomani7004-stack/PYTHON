
def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def main():
    students = []

    print("=== Student Grade Management System ===")

    while True:
        name = input("\nEnter student name (or 'exit' to finish): ")

        if name.lower() == "exit":
            break

        try:
            marks = float(input("Enter marks (0-100): "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                continue

            students.append({
                "name": name,
                "marks": marks,
                "grade": calculate_grade(marks)
            })

        except ValueError:
            print("Please enter valid numeric marks.")

    if not students:
        print("No student records available.")
        return

    print("\n--- Student Report ---")
    for student in students:
        print(
            f"Name: {student['name']} | "
            f"Marks: {student['marks']:.2f} | "
            f"Grade: {student['grade']}"
        )

    average = sum(s["marks"] for s in students) / len(students)
    topper = max(students, key=lambda s: s["marks"])

    print(f"\nClass Average: {average:.2f}")
    print(f"Topper: {topper['name']} ({topper['marks']:.2f})")


if __name__ == "__main__":
    main()
