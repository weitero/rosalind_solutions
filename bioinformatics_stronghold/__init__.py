import typing
from io import StringIO


def read_fasta(fh: typing.IO):
    """
    >>> read_fasta(StringIO('>Rosalind_6404\\nCCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC\\nTCCCACTAATAATTCTGAGG\\n>Rosalind_5959\\nCCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT\\nATATCCATTTGTCAGCAGACACGC\\n'))
    {'Rosalind_6404': 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG', 'Rosalind_5959': 'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC'}
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
    return d
