import typing
from io import StringIO

import __init__
dna_solve_it = __import__('dna-counting_dna_nucleotides')


def solve_it(fh: typing.IO):
    """
    Return a consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

    >>> solve_it(StringIO('>Rosalind_1\\nATCCAGCT\\n>Rosalind_2\\nGGGCAACT\\n>Rosalind_3\\nATGGATCT\\n>Rosalind_4\\nAAGCAACC\\n>Rosalind_5\\nTTGGAACT\\n>Rosalind_6\\nATGCCATT\\n>Rosalind_7\\nATGGCACT\\n'))
    ATGCAACT
    A: 5 1 0 0 5 5 0 0
    C: 0 0 1 4 2 0 6 1
    G: 1 1 6 3 0 1 0 0
    T: 1 5 0 0 0 1 1 6
    """
    def helper(s: str):
        return dict(zip('ACGT', dna_solve_it.solve_it(s)))

    d = __init__.read_fasta(fh)
    base_m = [''.join(l) for l in zip(*d.values())]
    count_m = [helper(s) for s in base_m]

    cs = ''.join([max(d, key=d.get) for d in count_m])
    print(cs)

    for b in 'ACGT':
        print(f'{b}:', ' '.join([str(c[b]) for c in count_m]))
