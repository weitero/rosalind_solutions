def solve_it(f: str) -> None:
    """
    Return a file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

    >>> solve_it('sample_dataset')
    Yes, brave Sir Robin turned about
    And gallantly he chickened out
    Bravely talking to his feet
    He beat a very brave retreat
    """
    with open(f, 'r') as fh:
        contents = list(fh.readlines())
        for l in contents:
            if (contents.index(l) + 1) % 2 == 0:
                print(l.rstrip())
