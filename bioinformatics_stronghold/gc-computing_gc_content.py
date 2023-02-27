from decimal import Decimal


def solve_it(f: str) -> None:
    """
    Return the ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

    >>> solve_it('gc-sample_dataset')
    Rosalind_0808
    60.919540
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
    gc_d = {k: ((v.count('C') + v.count('G')) / len(v) * 100)
            for k, v in seq_d.items()}
    max_k = max(gc_d, key=gc_d.get)
    print(max_k)
    print(Decimal(gc_d[max_k]).quantize(Decimal('0.000000')))
