from collections import Counter


def solve_it(s: str) -> None:
    """
    Return the number of occurrences of each word `s`, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

    >>> solve_it('We tried list and we tried dicts also we tried Zen')
    We 1
    tried 3
    list 1
    and 1
    we 2
    dicts 1
    also 1
    Zen 1
    """
    for k, v in Counter(s.split(' ')).items():
        print(k, v)
