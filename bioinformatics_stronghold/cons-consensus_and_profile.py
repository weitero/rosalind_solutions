from collections import Counter


def solve_it(f: str) -> None:
    """
    Return a consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

    >>> solve_it('cons-sample_dataset')
    ATGCAACT
    A: 5 1 0 0 5 5 0 0
    C: 0 0 1 4 2 0 6 1
    G: 1 1 6 3 0 1 0 0
    T: 1 5 0 0 0 1 1 6
    """
    seq_d = {}
    with open(f, 'r') as fh:
        for l in fh:
            l = l.rstrip('\n')
            if l.startswith('>'):
                seq_k = l[1:]
                seq_d[seq_k] = ''
            else:
                seq_d[seq_k] = seq_d[seq_k] + l
    count_mat = [Counter(l) for l in zip(*seq_d.values())]
    consensus = ''.join([max(c, key=c.get) for c in count_mat])
    print(consensus)
    for b in 'ACGT':
        print(f'{b}:', ' '.join([str(c[b]) for c in count_mat]))
