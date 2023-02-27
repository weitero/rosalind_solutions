def solve_it(s: str) -> str:
    """
    Return the reverse complement `sc` of `s`.

    >>> solve_it('AAAACCCGGT')
    'ACCGGGTTTT'
    """
    rev_s = s[::-1]
    comp_rev_s = rev_s.translate(str.maketrans('ACGT', 'TGCA'))
    return comp_rev_s
