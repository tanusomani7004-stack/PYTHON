print("""
hello everyone.
here tannu somani
from section F 
date-27-10-2025
project gracebook analyser \n""")
print("""hello everyone 
Assignment title: Analyzing and reporting student grades  \n""")
def number():
    marks={}
    x=int(input("Enter the number of students you want:"))
    for i in range(x):
        student_name=input("enter the name of student:")
        total_marks=float(input(f"enter the total marks of {student_name}:"))
        marks[student_name]=total_marks
    print("marks=",marks)

    
    s=sum(marks.values())
    a=s/x
    print("the average number of students is:",a)

    import statistics as st
    values=list(marks.values())
    m=st.median(values)
    print("median number of students is:",m)

    max_value=max(marks.values())
    print("the maximum marks of student name is:",max_value)

    min_value=min(marks.values())
    print("the minimum marks of student name is:",min_value)

    student_grades = {}

    for student, score in marks.items():
        if score >= 90 and score<=100:
            student_grades[student] = "A"
        elif score >= 80 and score<=89:
            student_grades[student] = "B"
        elif score >= 70 and score<=79:
            student_grades[student] = "C"
        elif score >= 60 and score<=69:
            student_grades[student] = "D"
        else:
            student_grades[student] = "F"
            
    
    print("students grade is",student_grades)
    
    
    passed_students = [name for name, m in marks.items() if m >= 40]
    failed_students = [name for name, m in marks.items() if m < 40]
    print("Passed:", passed_students, "number of passed student:", len(passed_students))
    print("Failed:", failed_students, "number of fail student :", len(failed_students))
    
    def print_results_table(marks, student_grades):
        print("\nName\tMarks\tGrade")
        print("-" * 25)
        for student_name in marks:
            print(f"{student_name}\t{marks[student_name]}\t{student_grades[student_name]}")

    while True:
        print_results_table(marks, student_grades)
        choice = input("Do you want to analyze another class? (y/n): ")
        if choice.lower() != 'y':
            break
    
number()
