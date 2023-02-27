def solve_it(s: str) -> list[int]:
    """
    Returns four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occurs in `s`.

    >>> solve_it('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    [20, 12, 17, 21]
    """
    return [s.count(b) for b in 'ACGT']
