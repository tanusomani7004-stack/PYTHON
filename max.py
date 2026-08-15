marks = []


for i in range(5):
    m = int(input(f"Student {i+1} ke marks enter karo: "))
    marks.append(m)


highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark


total = 0
passed = 0
failed = 0

for mark in marks:
    total += mark

    if mark >= 40:
        passed += 1
    else:
        failed += 1

average = total / 5


print("\nMarks:", marks)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Passed:", passed)
print("Failed:", failed)
