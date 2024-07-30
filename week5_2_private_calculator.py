def min_operations(n):
    dp = [0] + [float('inf')] * n

    for i in range(1, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)  # Operation: +1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)  # Operation: x2
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)  # Operation: x3

    return dp[n]

if __name__ == '__main__':
    input_n = int(input())
    print(min_operations(input_n)-1)
