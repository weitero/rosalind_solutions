def solve_it(n: int):
    """
    Return the value of `Fn`.

    >>> solve_it(6)
    8
    """
    assert n <= 25

    if n < 2:
        return n
    return solve_it(n - 1) + solve_it(n - 2)
