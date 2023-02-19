from decimal import Decimal


def solve_it(k: int, m: int, n: int):
    """
    Return the probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

    >>> solve_it(2, 2, 2)
    0.78333
    """

    total = k + m + n
    p1 = k / total + (m / total) * (1 / 2)
    p2 = (n / total) * (k / (total - 1) + (m / (total - 1)) * (1 / 2)) + \
         ((m / total) * (1 / 2)) * (k / (total - 1) + ((m - 1) / (total - 1)) * (1 / 2))
    return float(Decimal(p1 + p2).quantize(Decimal('0.00000')))
