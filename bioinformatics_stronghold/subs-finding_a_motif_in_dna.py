def solve_it(s: str, t: str, i: int = 0) -> None:
    """
    Return all locations of `t` as a substring of `s`.

    >>> solve_it('GATATATGCATATACTT', 'ATAT')
    2
    4
    10
    """
    l = s.find(t, i) + 1
    if l:
        print(l)
        solve_it(s, t, i + l)
