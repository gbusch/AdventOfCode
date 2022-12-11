from typing import Tuple, Set, List


def parse_assignment_pair(ass_pair: str) -> Tuple[Set[int], Set[int]]:
    """
    >>> parse_assignment_pair("2-4,6-8")
    ({2, 3, 4}, {8, 6, 7})
    >>> parse_assignment_pair("6-6,4-6")
    ({6}, {4, 5, 6})
    """
    assignments = ass_pair.split(",")
    ass1 = assignments[0].split("-")
    ass2 = assignments[1].split("-")
    return (
        set(range(int(ass1[0]), int(ass1[1]) + 1)),
        set(range(int(ass2[0]), int(ass2[1]) + 1)),
    )


def fully_contained_in_other(assignments: Tuple[Set[int], Set[int]]) -> bool:
    """
    >>> fully_contained_in_other(({2, 3, 4}, {8, 6, 7}))
    False
    >>> fully_contained_in_other(({6}, {4, 5, 6}))
    True
    >>> fully_contained_in_other(({4, 5, 6}, {6}))
    True
    """
    return (assignments[0] & assignments[1] == assignments[0]) | (
        assignments[0] & assignments[1] == assignments[1]
    )


def any_overlap(assignments: Tuple[Set[int], Set[int]]) -> bool:
    """
    >>> any_overlap(({2, 3, 4}, {8, 6, 7}))
    False
    >>> any_overlap(({6}, {4, 5, 6}))
    True
    >>> any_overlap(({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}))
    True
    """
    return bool(assignments[0] & assignments[1])


def part1(assignment_list: List[str]) -> int:
    """
    >>> part1(["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"])
    2
    """
    return sum(
        [
            fully_contained_in_other(parse_assignment_pair(ass))
            for ass in assignment_list
        ]
    )


def part2(assignment_list: List[str]) -> int:
    """
    >>> part2(["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"])
    4
    """
    return sum([any_overlap(parse_assignment_pair(ass)) for ass in assignment_list])


if __name__ == "__main__":
    with open("data/day04.txt", "r") as f:
        assignment_list = f.read().split()

    print("part 1")
    print(part1(assignment_list))

    print("part 2")
    print(part2(assignment_list))
