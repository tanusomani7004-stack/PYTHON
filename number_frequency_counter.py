numbers = input("Enter numbers separated by space: ")

numbers = list(map(int, numbers.split()))

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1


print("\nNumber Frequency:")

for number, count in frequency.items():
    print(f"{number} → {count} time(s)")
