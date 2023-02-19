def solve_it(s: str):
    """
    Returns four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occurs in `s`.

    >>> solve_it('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    '20 12 17 21'
    """
    return ' '.join([str(s.count(x)) for x in ['A', 'C', 'G', 'T']])
