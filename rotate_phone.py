numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation value: "))

if len(numbers) == 0:
    print("List is empty.")

else:
    k = k % len(numbers)

    rotated = numbers[-k:] + numbers[:-k]

    print("Original list:", numbers)
    print("Rotated list :", rotated)
