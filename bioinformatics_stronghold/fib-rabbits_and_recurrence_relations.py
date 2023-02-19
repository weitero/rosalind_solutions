def solve_it(n: int, k: int):
    """
    Return the total number of rabbit pairs that will be present after `n` months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of `k` rabbit pairs (instead of only 1 pair).

    >>> solve_it(5, 3)
    19
    """
    assert n <= 40
    assert k <= 5

    if n <= 2:
        return 1
    else:
        reproductive = solve_it(n - 1, k)
        newborn = solve_it(n - 2, k) * k
        return reproductive + newborn
