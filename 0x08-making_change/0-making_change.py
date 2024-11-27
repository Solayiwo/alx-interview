#!/usr/bin/python3
"""Making Change Module"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given amount total.
    """
    if total <= 0:
        return 0

    # Initialize DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make total of 0

    # Update the DP array using each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check the result for the total amount
    return dp[total] if dp[total] != float('inf') else -1
