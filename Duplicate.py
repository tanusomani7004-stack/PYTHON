
def remove_duplicates(lst, index=0, result=[]):
    if index == len(lst):
        return result

    if lst[index] not in result:
        result.append(lst[index])

    return remove_duplicates(lst, index + 1, result)

n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    numbers.append(num)

unique = remove_duplicates(numbers)

print("Original List:", numbers)
print("List after removing duplicates:", unique)
