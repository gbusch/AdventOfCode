import numpy as np


def part1(input: str) -> int:
    """Part 1
    >>> part1('''0 3 6 9 12 15
    ... 1 3 6 10 15 21
    ... 10 13 16 21 30 45''')
    114
    """
    return sum(
        next_value(list(map(int, line.split())))
        for line in input.splitlines()
        if line.strip()
    )


def part2(input: str) -> int:
    """Part 2
    >>> part2('''0 3 6 9 12 15
    ... 1 3 6 10 15 21
    ... 10 13 16 21 30 45''')
    2
    """
    return sum(
        first_value(list(map(int, line.split())))
        for line in input.splitlines()
        if line.strip()
    )


def next_value(input: list[int]) -> int:
    """Returns the next value in the sequence
    >>> next_value([0, 3, 6, 9, 12, 15])
    18
    >>> next_value([-3, 0, 3, 6, 9, 12, 15])
    18
    >>> next_value([1, 3, 6, 10, 15, 21])
    28
    >>> next_value([10, 13, 16, 21, 30, 45])
    68
    """
    array = np.array(input)
    last_values = [array[-1]]
    while not all(a == 0 for a in array):
        array = array[1:] - array[:-1]
        last_values.append(array[-1])
    return sum(last_values)


def first_value(input: list[int]) -> int:
    """Returns the first value in the sequence
    >>> first_value([0, 3, 6, 9, 12, 15])
    -3
    >>> first_value([1, 3, 6, 10, 15, 21])
    0
    >>> first_value([10, 13, 16, 21, 30, 45])
    5
    """
    array = np.array(input)[::-1]
    last_values = [array[-1]]
    while not all(a == 0 for a in array):
        array = array[1:] - array[:-1]
        last_values.append(array[-1])
    return sum(last_values)


if __name__ == "__main__":
    with open("2023/data/day09.txt") as file:
        input = file.read()
    p1 = part1(input)
    assert p1 == 1901217887, f"Part 1 is {p1}, expected 1901217887"
    print(p1)
    print(part2(input))
