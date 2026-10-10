def analyze_lcs(first, second):
    m, n = len(first), len(second)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    sequence = []

    while i > 0 and j > 0:
        if first[i - 1] == second[j - 1]:
            sequence.append(first[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    sequence.reverse()

    return {
        "first_length": m,
        "second_length": n,
        "lcs_length": dp[m][n],
        "lcs_string": "".join(sequence) if dp[m][n] else "None",
        "dp_table_size": f"{m + 1} x {n + 1}",
        "dp_cell_computations": m * n,
        "time_complexity": "O(m*n)",
        "space_complexity": "O(m*n)"
    }


def main():
    first = input("Enter first string: ")
    second = input("Enter second string: ")

    result = analyze_lcs(first, second)

    print("\n--- LCS Analysis Report ---")
    print(f"First String Length: {result['first_length']}")
    print(f"Second String Length: {result['second_length']}")
    print(f"LCS Length: {result['lcs_length']}")
    print(f"LCS String: {result['lcs_string']}")
    print(f"DP Table Size: {result['dp_table_size']}")
    print(f"DP Cell Computations: {result['dp_cell_computations']}")
    print(f"Time Complexity: {result['time_complexity']}")
    print(f"Space Complexity: {result['space_complexity']}")
    print("Observation: Dynamic Programming avoids repeated calculations.")


if __name__ == "__main__":
    main()
