def change(money):
    # Initialize a list to store minimum coins needed for each value from 0 to money
    dp = [float('inf')] * (money + 1)
    dp[0] = 0  # 0 coins are needed to make a change for 0
    
    ##print("dp: ", dp)
    # Denominations of coins
    denominations = [1, 3, 4]
    
    # Iterate through each value from 1 to money and calculate minimum coins needed
    for i in range(1, money + 1):
        ##print("************************** i: ", i)
        for coin in denominations:
            ##print("*: ", coin)
            # Check if using the current coin is possible
            if i >= coin:
                ##print("dp[i]", dp[i], " dp[", i-coin, "] + 1: ", dp[i-coin], " + 1")
                dp[i] = min(dp[i], dp[i - coin] + 1)
                ##print("min_coins: " , dp[i])
    ##print("dp: ", dp)
    # The minimum number of coins needed to make change for 'money' is stored at dp[money]
    return dp[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
