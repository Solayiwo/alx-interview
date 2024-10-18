#!/usr/bin/python3
"""Define function for minimum operations"""


def minOperations(n):
    """
    Calculate the minimum number of operations to reach exactly 'n'
    characters in a text editor.
    Operations allowed:
    - Copy All
    - Paste
    The objective is to find the fewest operations needed to
    achieve 'n' characters.

    Args:
    n (int): The target number of characters.

    Returns:
    int: The minimum number of operations to reach 'n' characters.
    Returns 0 if n <= 1.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
