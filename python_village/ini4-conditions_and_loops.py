def solve_it(a: int, b: int):
    """
    Return the sum of all odd integers from `a` through `b`, inclusively.

    >>> solve_it(100, 200)
    7500
    """
    assert a < b < 10000

    if b - a == 1:
        if a % 2 ==0:
            return 0
        return a
    else:
        if a % 2 == 0:
            return solve_it(a + 1, b)
        return a + solve_it(a + 1, b)
