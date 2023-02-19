def solve_it(s: str, t: str, l: int = 0):
    """
    Return all locations of `t` as a substring of `s`.

    >>> solve_it('GATATATGCATATACTT', 'ATAT')
    2
    4
    10
    """
    if t in s:
        i = s.index(t) + 1
        l = i + l
        print(l)
        solve_it(s[i:], t, l)
