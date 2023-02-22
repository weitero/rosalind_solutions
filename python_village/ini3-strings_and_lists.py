def solve_it(s: str, a: int, b: int, c: int, d: int):
    """
    Return the slice of this string from indices `a` through `b` and `c` through `d` (with space in between), inclusively. In other words, we should include elements `s[b]` and `s[d]` in our slice.

    >>> solve_it('HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.', 22, 27, 97, 102)
    Humpty
    Dumpty
    """
    print(s[a:b+1])
    print(s[c:d+1])
