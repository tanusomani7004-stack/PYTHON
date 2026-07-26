def sum_n(n):
    if n == 1:         
        return 1
    return n + sum_n(n - 1)

n = int(input("Enter a number: "))

if n > 0:
    print("Sum of first", n, "numbers is:", sum_n(n))
else:
    print("Please enter a positive integer.")
