from collections import Counter


def part1(left_list, right_list):
    """
    >>> part1([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    11
    """
    return sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list)))


def part2(left_list, right_list):
    """
    >>> part2([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    31
    """
    counts = Counter(right_list)
    return sum(l * counts[l] for l in left_list)


def parse(inp):
    """
    >>> parse('''3   4
    ... 4   3
    ... 2   5
    ... 1   3
    ... 3   9
    ... 3   3''')
    ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    """
    left, right = map(list, zip(*[map(int, line.split()) for line in inp.split("\n")]))
    return left, right


if __name__ == "__main__":
    with open("2024/data/day01.txt", "r") as f:
        left_list, right_list = parse(f.read())
    print(f"Part 1: {part1(left_list, right_list)}")
    print(f"Part 2: {part2(left_list, right_list)}")
