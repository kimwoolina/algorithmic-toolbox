def can_partition_equal_sum(values):
    total_sum = sum(values)
    if total_sum % 3 != 0:
        return False
    
    subset_sum = total_sum // 3
    visited = [False] * len(values)

    def backtrack(index, subset_count, current_sum):
        if subset_count == 3:
            return True

        if current_sum == subset_sum:
            return backtrack(0, subset_count + 1, 0)

        for i in range(index, len(values)):
            if not visited[i] and current_sum + values[i] <= subset_sum:
                visited[i] = True
                if backtrack(i + 1, subset_count, current_sum + values[i]):
                    return True
                visited[i] = False

        return False

    return backtrack(0, 0, 0)

def partition3(values):
    if can_partition_equal_sum(values):
        return 1
    else:
        return 0

if __name__ == '__main__':
    input_n = int(input())
    input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))


# def can_partition_equal_sum(subset_sum, num_elements, values):
#     dp = [[[False for _ in range(subset_sum + 1)] for _ in range(subset_sum + 1)] for _ in range(subset_sum + 1)]
    
#     for i in range(subset_sum + 1):
#         for j in range(subset_sum + 1):
#             for k in range(subset_sum + 1):
#                 if i == 0 and j == 0 and k == 0:
#                     dp[i][j][k] = True
#                 elif i >= values[0] and j >= values[1] and k >= values[2]:
#                     dp[i][j][k] = dp[i - values[0]][j - values[1]][k - values[2]] or dp[i][j][k]
#                 elif i >= values[0] and j >= values[1]:
#                     dp[i][j][k] = dp[i - values[0]][j - values[1]][k] or dp[i][j][k]
#                 elif i >= values[0]:
#                     dp[i][j][k] = dp[i - values[0]][j][k] or dp[i][j][k]

#     return dp[subset_sum][subset_sum][subset_sum]

# def partition3(values):
#     total_sum = sum(values)
#     if total_sum % 3 != 0:
#         return 0

#     subset_sum = total_sum // 3
#     num_elements = len(values)
#     if can_partition_equal_sum(subset_sum, num_elements, values):
#         return 1
#     else:
#         return 0

# if __name__ == '__main__':
#     input_n = int(input())
#     input_values = list(map(int, input().split()))
#     assert input_n == len(input_values)
#     print(partition3(input_values))
