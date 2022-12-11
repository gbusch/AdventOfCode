from typing import List, Set, Iterator
from functools import reduce


def part1(rucksacks: List[str]) -> int:
    """
    >>> part1([
    ...    "vJrwpWtwJgWrhcsFMMfFFhFp",
    ...    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    ...    "PmmdzqPrVvPwwTWBwg",
    ...    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    ...    "ttgJtRGJQctTZtZT",
    ...    "CrZsJsPPZsGzwwsLwLmpwMDw",
    ... ])
    157
    """
    return sum([get_priority(find_overlap_item(rucksack)) for rucksack in rucksacks])


def part2(rucksacks: List[str]) -> int:
    """
    >>> part2([
    ...    "vJrwpWtwJgWrhcsFMMfFFhFp",
    ...    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    ...    "PmmdzqPrVvPwwTWBwg",
    ...    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    ...    "ttgJtRGJQctTZtZT",
    ...    "CrZsJsPPZsGzwwsLwLmpwMDw",
    ... ])
    70
    """
    return sum(
        [
            get_priority(get_group_batch(group))
            for group in list(group_of_three(rucksacks))
        ]
    )


def find_overlap_item(content: str) -> str:
    """
    >>> find_overlap_item("vJrwpWtwJgWrhcsFMMfFFhFp")
    'p'
    >>> find_overlap_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    'L'
    >>> find_overlap_item("PmmdzqPrVvPwwTWBwg")
    'P'
    >>> find_overlap_item("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    'v'
    >>> find_overlap_item("ttgJtRGJQctTZtZT")
    't'
    >>> find_overlap_item("CrZsJsPPZsGzwwsLwLmpwMDw")
    's'
    """
    compartment_size = len(content) // 2
    compartment1 = set(content[:compartment_size])
    compartment2 = set(content[compartment_size:])
    return compartment1.intersection(compartment2).pop()


def get_group_batch(rucksacks: List[str]) -> str:
    """
    >>> get_group_batch(["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"])
    'r'
    >>> get_group_batch(["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"])
    'Z'
    """
    sets: List[Set[str]] = [set(r) for r in rucksacks]
    return reduce(lambda x, y: x.intersection(y), sets).pop()


def get_priority(item: str) -> int:
    """
    >>> get_priority('a')
    1
    >>> get_priority('A')
    27
    >>> get_priority('p')
    16
    >>> get_priority('P')
    42
    """
    unicode = ord(item)
    return unicode - 96 if unicode >= 97 else unicode - 38


def group_of_three(big_list: List[str]) -> Iterator[List[str]]:
    """
    >>> big_list = ["a", "b", "c", "d", "e", "f"]
    >>> list(group_of_three(big_list))
    [['a', 'b', 'c'], ['d', 'e', 'f']]
    """
    for i in range(0, len(big_list), 3):
        yield big_list[i : i + 3]


if __name__ == "__main__":
    with open("data/day03.txt", "r") as f:
        rucksacks = f.read().split()

    print("part 1")
    print(part1(rucksacks))

    print("part 2")
    print(part2(rucksacks))
