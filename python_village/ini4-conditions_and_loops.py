def solve_it(a: int, b: int) -> int:
    """
    Return the sum of all odd integers from `a` through `b`, inclusively.

    >>> solve_it(100, 200)
    7500
    """
    sum = 0
    while a < b:
        if a % 2 == 1:
            sum = sum + a
            a = a + 2
        else:
            a = a + 1
    return sum
