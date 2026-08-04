
def second_largest(lst, index, largest, second):
    if index == len(lst):
        return second

    if lst[index] > largest:
        second = largest
        largest = lst[index]
    elif lst[index] > second and lst[index] != largest:
        second = lst[index]

    return second_largest(lst, index + 1, largest, second)

n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    numbers.append(num)

result = second_largest(numbers, 0, float('-inf'), float('-inf'))

if result == float('-inf'):
    print("There is no second largest element.")
else:
    print("Second Largest Number is:", result)
