def find_mirror(input: str) -> int:
    """
    >>> find_mirror('''#.##..##.
    ... ..#.##.#.
    ... ##......#
    ... ##......#
    ... ..#.##.#.
    ... ..##..##.
    ... #.#.##.#.''')
    5
    >>> find_mirror('''#...##..#
    ... #....#..#
    ... ..##..###
    ... #####.##.
    ... #####.##.
    ... ..##..###
    ... #....#..#''')
    400
    """
    mirrors = []
    for row in input.splitlines():
        mirrors.append(set(find_mirror_single(row)))
    inters = set.intersection(*mirrors)
    if inters:
        return min(inters)
    mirrors = []
    for col in zip(*input.splitlines()):
        mirrors.append(set(find_mirror_single("".join(col))))
    inters = set.intersection(*mirrors)
    return min(inters)*100


def find_mirror_single(input: str) -> int:
    """
    >>> list(find_mirror_single('#.##..##.'))
    [5, 7]
    >>> list(find_mirror_single('##......#'))
    [1, 5]
    """
    input_forw = list(input)
    input_backw = list(input)[::-1]
    for i in range(1, len(input_forw)):
        forw = input_forw[i:min(2*i, len(input))]
        backw = input_backw[len(input)-i:2*(len(input)-i)]
        if forw == backw:
            yield i

if __name__ == "__main__":
    with open("2023/data/day13.txt", "r") as f:
        input = f.read().split("\n\n")
    
    p1 = sum(find_mirror(i) for i in input)
    print(f"Part 1: {p1}")