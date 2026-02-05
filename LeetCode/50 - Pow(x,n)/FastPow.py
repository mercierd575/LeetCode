def myPow(x: float, n: int) -> float:
    """Uses the fast exponentiation algorithm to find the nth power of x in an O(log n) complexity"""
    if n == 0:
        return 1
    else:
        if n < 0:
            x = 1 / x
            n = -1 * n
        # If n is even, we calculate b^(n//2) and multiply it with itself
        # If n is odd, we calculate b^(n//2) and multiply it with itself and n
        m = myPow(x, n // 2)
        k = 1
        if n % 2 != 0:
            k = x
        return m * m * k
