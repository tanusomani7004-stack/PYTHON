
num = int(input("Enter a positive decimal number: "))

if num < 0:
    print("Please enter a positive number.")

elif num == 0:
    print("Binary: 0")

else:
    binary = ""

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    print("Binary:", binary)
