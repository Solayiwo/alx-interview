#!/usr/bin/python3
"""Prime Game module"""

def isWinner(x, nums):
    """
    Determines the winner of a prime game played over x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers where nums[i] is the maximum
        number for the ith round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
             If there is a tie, returns None.
    """
    def sieve_of_eratosthenes(max_n):
        """Precompute primes up to max_n using Sieve of Eratosthenes."""
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        for i in range(2, int(max_n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    max_n = max(nums)
    original_primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        is_prime = original_primes[:n + 1]  # Copy primes for this round
        moves = 0
        for i in range(2, n + 1):
            if is_prime[i]:
                moves += 1
                for j in range(i, n + 1, i):
                    is_prime[j] = False
        # Maria wins if moves are odd; Ben wins if even
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
