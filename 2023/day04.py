from collections import defaultdict


def part1(input: str) -> int:
    """Part 1
    >>> part1('''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    ... Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    ... Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    ... Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    ... Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    ... Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11''')
    13
    """
    return sum(
        calculate_points(get_winning_numbers(card)) for card in input.split("\n")
    )


def part2(input: str) -> int:
    """Part 2
    >>> part2('''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    ... Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    ... Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    ... Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    ... Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    ... Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11''')
    30
    """
    return sum(win_cards(input).values())


def win_cards(input: str) -> defaultdict[int, int]:
    """Play with winning cards.
    >>> win_cards('''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    ... Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    ... Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    ... Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    ... Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    ... Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11''')
    defaultdict(<class 'int'>, {0: 1, 1: 2, 2: 4, 3: 8, 4: 14, 5: 1})
    """
    instances: defaultdict[int, int] = defaultdict(int)
    for i, card in enumerate(input.split("\n")):
        instances[i] += 1
        for wins in range(len(get_winning_numbers(card))):
            instances[i + wins + 1] += instances[i]
    return instances


def get_winning_numbers(input: str) -> list[int]:
    """Get the winning numbers from the input.
    >>> sorted(get_winning_numbers('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'))
    [17, 48, 83, 86]
    """
    return [
        int(x)
        for x in set(input.split(":")[1].split("|")[1].split())
        & set(input.split(":")[1].split("|")[0].split())
    ]


def calculate_points(winning_numbers: list[int]) -> int:
    """Calculate the points of the winning numbers.
    >>> calculate_points([17, 48, 83, 86])
    8
    >>> calculate_points([1, 21])
    2
    >>> calculate_points([])
    0
    """
    return 0 if len(winning_numbers) == 0 else 2 ** (len(winning_numbers) - 1)


if __name__ == "__main__":
    with open("2023/data/day04.txt", "r") as f:
        input = f.read()
    print(part1(input))
    print(part2(input))
