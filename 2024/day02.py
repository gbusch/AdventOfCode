def part1(reports):
    """
    >>> part1([[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]])
    2
    """
    return sum(safety_check(report) for report in reports)


def part2(reports):
    """
    >>> part2([[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]])
    4
    """
    return sum(safety_check_with_dampener(report) for report in reports)


def safety_check(report):
    """
    >>> safety_check([1, 1])
    False
    >>> safety_check([7, 6, 4, 2, 1])
    True
    >>> safety_check([1, 2, 7, 8, 9])
    False
    >>> safety_check([9, 7, 6, 2, 1])
    False
    >>> safety_check([1, 3, 2, 4, 5])
    False
    >>> safety_check([8, 6, 4, 4, 1])
    False
    >>> safety_check([1, 3, 6, 7, 9])
    True
    """
    prev = None
    incr = None
    for level in report:
        if not prev:
            prev = level
            continue
        if not incr:
            incr = 1 if (level - prev) > 0 else -1

        if (prev == level) or (abs(level - prev) > 3) or ((level - prev) * incr < 0):
            return False
        prev = level
    return True


def safety_check_with_dampener(report):
    """
    >>> safety_check_with_dampener([7, 6, 4, 2, 1])
    True
    >>> safety_check_with_dampener([1, 2, 7, 8, 9])
    False
    >>> safety_check_with_dampener([9, 7, 6, 2, 1])
    False
    >>> safety_check_with_dampener([1, 3, 2, 4, 5])
    True
    >>> safety_check_with_dampener([8, 6, 4, 4, 1])
    True
    >>> safety_check_with_dampener([1, 3, 6, 7, 9])
    True
    """
    if safety_check(report):
        return True
    for i, _ in enumerate(report):
        if safety_check(report[:i] + report[i + 1 :]):
            return True
    return False


if __name__ == "__main__":
    with open("2024/data/day02.txt", "r") as f:
        data = [[int(l) for l in line.strip().split()] for line in f]

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
