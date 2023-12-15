def find_mirror(input: str) -> int:
    """
    >>> find_mirror('#.##..##.')
    5
    """
    input_forw = list(input)
    input_backw = list(input)[::-1]
    for i in range(1, len(input_forw)):
        forw = input_forw[i:min(2*i, len(input))]
        backw = input_backw[len(input)-i:2*(len(input)-i)]
        if forw == backw:
            return i