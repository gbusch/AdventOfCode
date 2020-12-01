def part1(inlist):
    """
    >>> inlist = [1721, 979, 366, 299, 675, 1456]
    >>> part1(inlist)
    514579
    """
    for ix, x in enumerate(inlist):
        for _, y in enumerate(inlist[ix+1:]):
            if (x + y) == 2020:
                return x * y


def part2(inlist):
    """
    >>> inlist = [1721, 979, 366, 299, 675, 1456]
    >>> part2(inlist)
    241861950
    """
    for ix, x in enumerate(inlist):
        for iy, y in enumerate(inlist[ix+1:]):
            for _, z in enumerate(inlist[iy+1:]):
                if (x + y + z) == 2020:
                    return x * y * z


if __name__ == "__main__":
    with open("data/day01.txt", "r") as f:
        inlist = [int(x) for x in f.read().split()]
    
    print("PART 1")
    print(part1(inlist))

    print("PART 2")
    print(part2(inlist))
