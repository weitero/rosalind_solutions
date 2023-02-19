import typing

from decimal import Decimal
from io import StringIO


def solve_it(fh: typing.IO):
    """
    Return the ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

    >>> solve_it(StringIO('>Rosalind_6404\\nCCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC\\nTCCCACTAATAATTCTGAGG\\n>Rosalind_5959\\nCCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT\\nATATCCATTTGTCAGCAGACACGC\\n>Rosalind_0808\\nCCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC\\nTGGGAACCTGCGGGCAGTAGGTGGAAT\\n'))
    Rosalind_0808
    60.919540
    """

    d = {}
    k = ''
    for l in fh.readlines():
        l = l.rstrip('\n')
        if l.startswith('>'):
            k = l[1:]
            d[k] = ''
        else:
            d[k] = d[k] + l

    def helper(s: str):
        return (s.count('G') + s.count('C')) / len(s) * 100
    d2 = {k: helper(d[k]) for k in d}

    max_k = max(d2, key=d2.get)
    print(max_k)
    print(Decimal(d2[max_k]).quantize(Decimal('0.000000')))
