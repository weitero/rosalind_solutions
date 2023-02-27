def solve_it(s: str, t: str) -> int:
    """
    Return the Hamming distance `dH(s, t)`.

    >>> solve_it('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')
    7
    """
    if len(s) == 1:
        return int(s != t)
    return int(s[0] != t[0]) + solve_it(s[1:], t[1:])
