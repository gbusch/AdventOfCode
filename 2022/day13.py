from itertools import zip_longest
from functools import cmp_to_key


def compare_packets(packet1, packet2):
    """
    >>> compare_packets([1, 1], [1, 2])
    1
    >>> compare_packets([2, 1], [1, 1])
    -1
    >>> compare_packets([1, 1], [1, 1, 1])
    1
    >>> compare_packets([1, 1, 1], [1, 1])
    -1
    >>> compare_packets([], [3])
    1
    >>> compare_packets([[1], [2, 3, 4]], [[1], 4])
    1
    >>> compare_packets([9], [[8, 7, 6]])
    -1
    >>> compare_packets([[4, 4], 4, 4], [[4, 4], 4, 4, 4])
    1
    >>> compare_packets([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9])
    -1
    >>> compare_packets([[[]]], [[]])
    -1
    """
    match (packet1, packet2):
        case (int(), int()):
            if packet1 < packet2:
                return 1
            elif packet1 > packet2:
                return -1
            else:
                return 0
        case (int(), list()):
            return compare_packets([packet1], packet2)
        case (list(), int()):
            return compare_packets(packet1, [packet2])
        case (list(), list()):
            if packet1 is None:
                return 1
            elif packet2 is None:
                return -1
            else:
                for p1, p2 in zip_longest(packet1, packet2):
                    if p1 is None:
                        return 1
                    elif p2 is None:
                        return -1
                    else:
                        comp = compare_packets(p1, p2)
                        if comp != 0:
                            return comp
                return 0


EXAMPLE_INPUT = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


import json


def part1(inp):
    inp = [
        [json.loads(packet) for packet in pair.split()] for pair in inp.split("\n\n")
    ]

    right_order_indices = [
        i + 1 for i, pair in enumerate(inp) if compare_packets(*pair) > 0
    ]
    return sum(right_order_indices)


def part2(inp):
    inp = [json.loads(packet) for pair in inp.split("\n\n") for packet in pair.split()]
    separators = [[[2]], [[6]]]
    inp.extend(separators)
    inp.sort(key=cmp_to_key(compare_packets), reverse=True)
    divider_pos = [inp.index(sep) for sep in separators]
    return (divider_pos[0] + 1) * (divider_pos[1] + 1)


if __name__ == "__main__":
    assert part1(EXAMPLE_INPUT) == 13
    assert part2(EXAMPLE_INPUT) == 140

    with open("data/day13.txt", "r") as f:
        data = f.read()

    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")
