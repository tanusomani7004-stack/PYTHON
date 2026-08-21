numbers = list(map(int, input("Enter numbers separated by space: ").split()))

num_set = set(numbers)

longest_sequence = []
longest_length = 0

for num in num_set:

    # Check if num is the starting point
    if num - 1 not in num_set:

        current = num
        current_sequence = [current]

        # Find consecutive numbers
        while current + 1 in num_set:
            current += 1
            current_sequence.append(current)

        # Update longest sequence
        if len(current_sequence) > longest_length:
            longest_length = len(current_sequence)
            longest_sequence = current_sequence

print("Longest Consecutive Sequence:", longest_sequence)
print("Length:", longest_length)
