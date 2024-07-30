def edit_distance(first_string, second_string):
    m, n = len(first_string), len(second_string)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if first_string[i - 1] == second_string[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                           dp[i][j - 1] + 1,      # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution
    print("dp: ", dp)
    return dp[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
