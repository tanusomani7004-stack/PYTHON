def compare_bubble_insertion(random_data, sorted_data, reverse_data):

    def bubble_sort(arr):
        a = arr[:]
        comparisons = 0
        swaps = 0
        n = len(a)

        for i in range(n - 1):
            swapped = False

            for j in range(n - 1 - i):
                comparisons += 1

                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swaps += 1
                    swapped = True

            if not swapped:
                break

        return a, comparisons, swaps

    def insertion_sort(arr):
        a = arr[:]
        comparisons = 0
        shifts = 0

        for i in range(1, len(a)):
            key = a[i]
            j = i - 1

            while j >= 0:
                comparisons += 1

                if a[j] > key:
                    a[j + 1] = a[j]
                    shifts += 1
                    j -= 1
                else:
                    break

            a[j + 1] = key

        return a, comparisons, shifts

    result = ["Sorting Performance Report"]

    datasets = [
        ("Random Dataset", random_data),
        ("Sorted Dataset", sorted_data),
        ("Reverse Dataset", reverse_data)
    ]

    for name, data in datasets:
        bubble_result, bubble_comp, bubble_swaps = bubble_sort(data)
        insertion_result, insertion_comp, insertion_shifts = insertion_sort(data)

        result.append(name)

        result.append("Bubble Sorted: " + " ".join(map(str, bubble_result)))
        result.append("Bubble Comparisons: " + str(bubble_comp))
        result.append("Bubble Swaps: " + str(bubble_swaps))

        result.append("Insertion Sorted: " + " ".join(map(str, insertion_result)))
        result.append("Insertion Comparisons: " + str(insertion_comp))
        result.append("Insertion Shifts: " + str(insertion_shifts))

        if bubble_comp < insertion_comp:
            result.append("Better Algorithm: Bubble Sort")
        elif insertion_comp < bubble_comp:
            result.append("Better Algorithm: Insertion Sort")
        else:
            result.append("Better Algorithm: Both Equal")

    return result
