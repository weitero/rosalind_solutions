def solve_it(t: str):
    """
    Return the transcribed RNA string of `t`.

    >>> solve_it('GATGGAACTTGACTACGTAAATT')
    'GAUGGAACUUGACUACGUAAAUU'
    """
    return t.replace('T', 'U')
