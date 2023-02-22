def solve_it(s: str):
    """
    Return the reverse complement `sc` of `s`.

    >>> solve_it('AAAACCCGGT')
    'ACCGGGTTTT'
    """
    bp = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A',
    }
    rev_s = s[::-1]
    comp_rev_s = rev_s.translate(str.maketrans('ACGT', 'TGCA'))
    return comp_rev_s
