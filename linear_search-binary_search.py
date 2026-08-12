def compare_search_algorithms(arr, target):

    def linear_search(arr, key):
        comparison = 0

        for i in range(len(arr)):
            comparison += 1

            if arr[i] == key:
                return i, comparison

        return -1, comparison

    def binary_search(arr, key):
        low = 0
        high = len(arr) - 1
        comparison = 0
        result = -1

        while low <= high:
            comparison += 1
            mid = (low + high) // 2

            if arr[mid] == key:
                result = mid
                high = mid - 1

            elif arr[mid] < key:
                low = mid + 1

            else:
                high = mid - 1

        return result, comparison

    linear_index, linear_comparisons = linear_search(arr, target)
    binary_index, binary_comparisons = binary_search(arr, target)

    if linear_comparisons < binary_comparisons:
        better = "Linear Search"
    elif binary_comparisons < linear_comparisons:
        better = "Binary Search"
    else:
        better = "Both Equal"

    return [
        "Search Comparison Report",
        "Linear Search",
        f"Index: {linear_index}",
        f"Comparisons: {linear_comparisons}",
        "Binary Search",
        f"Index: {binary_index}",
        f"Comparisons: {binary_comparisons}",
        f"Better Algorithm: {better}"
    ]
