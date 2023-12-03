import re
from collections import namedtuple

from typing import Iterator

SymbolPos = namedtuple("SymbolPos", "symbol x y")
NumberPos = namedtuple("NumberPos", "number y left right")


def part1(input: str) -> int:
    """Sum the valid part numbers.
    >>> part1('''467..114..
    ... ...*......
    ... ..35..633.
    ... ......#...
    ... 617*......
    ... .....+.58.
    ... ..592.....
    ... ......755.
    ... ...$.*....
    ... .664.598..''')
    4361
    """
    symbols = find_symbols(input)
    return sum(
        number.number
        for number in find_numbers(input)
        if is_part_number(number, symbols)
    )


def part2(input: str) -> int:
    """Sum the gear ratios.
    >>> part2('''467..114..
    ... ...*......
    ... ..35..633.
    ... ......#...
    ... 617*......
    ... .....+.58.
    ... ..592.....
    ... ......755.
    ... ...$.*....
    ... .664.598..''')
    467835
    """
    symbols = find_symbols(input)
    numbers = find_numbers(input)
    return sum(gear_ratio(symbol, numbers) for symbol in symbols)


def find_numbers(input: str) -> list[NumberPos]:
    """Find all numbers in a string.
    >>> find_numbers('''467..114..
    ... ...*......
    ... ..35......''')
    [NumberPos(number=467, y=0, left=0, right=2), NumberPos(number=114, y=0, left=5, right=7), NumberPos(number=35, y=2, left=2, right=3)]
    """
    return [
        NumberPos(number, y, left, right)
        for y, line in enumerate(input.splitlines())
        for number, left, right in find_number(line)
    ]


def find_number(line: str) -> Iterator[tuple[int, int, int]]:
    """Find all numbers in a line.
    >>> list(find_number('467..114..'))
    [(467, 0, 2), (114, 5, 7)]
    >>> list(find_number('35..35..35'))
    [(35, 0, 1), (35, 4, 5), (35, 8, 9)]
    """
    numbers = re.findall(r"\d+", line)
    l_search = 0
    for number in numbers:
        left = line.find(number, l_search)
        right = left + len(number) - 1
        yield (int(number), left, right)
        l_search = right + 1


def find_symbols(input: str) -> list[SymbolPos]:
    """Find all symbols in a string.
    >>> find_symbols('''467..114..
    ... ...*......
    ... ..35..633.
    ... ......#...''')
    [SymbolPos(symbol='*', x=3, y=1), SymbolPos(symbol='#', x=6, y=3)]
    """
    return [
        SymbolPos(char, x, y)
        for y, line in enumerate(input.splitlines())
        for x, char in enumerate(line)
        if char not in "0123456789."
    ]


def is_part_number(number: NumberPos, symbols: list[SymbolPos]) -> bool:
    """Check if a part number is valid.
    >>> is_part_number(NumberPos(467, 0, 0, 2), [SymbolPos('*', 3, 1), SymbolPos('*', 6, 3)])
    True
    >>> is_part_number(NumberPos(114, 0, 5, 7), [SymbolPos('*', 3, 1), SymbolPos('*', 6, 3)])
    False
    >>> is_part_number(NumberPos(35, 2, 2, 4), [SymbolPos('*', 3, 1), SymbolPos('*', 6, 3)])
    True
    """
    return any(
        symbol.x >= number.left - 1
        and symbol.x <= number.right + 1
        and symbol.y >= number.y - 1
        and symbol.y <= number.y + 1
        for symbol in symbols
    )


def gear_ratio(symbol: SymbolPos, numbers: list[NumberPos]) -> int:
    """Check if a symbol is a gear.
    >>> gear_ratio(SymbolPos('*', 3, 1), [NumberPos(467, 0, 0, 2), NumberPos(114, 0, 5, 7), NumberPos(35, 2, 2, 4)])
    16345
    >>> gear_ratio(SymbolPos('#', 3, 1), [NumberPos(467, 0, 0, 2), NumberPos(114, 0, 5, 7), NumberPos(35, 2, 2, 4)])
    0
    >>> gear_ratio(SymbolPos('*', 3, 1), [NumberPos(467, 0, 0, 2), NumberPos(114, 0, 5, 7)])
    0
    """
    adj_numbers = [
        number.number
        for number in numbers
        if symbol.symbol == "*"
        and symbol.x >= number.left - 1
        and symbol.x <= number.right + 1
        and symbol.y >= number.y - 1
        and symbol.y <= number.y + 1
    ]
    if len(adj_numbers) == 2:
        return adj_numbers[0] * adj_numbers[1]
    return 0


if __name__ == "__main__":
    with open("2023/data/day03.txt") as f:
        input = f.read()
    sol_part1 = part1(input)
    print(sol_part1)
    assert sol_part1 == 532331
    sol_part2 = part2(input)
    print(sol_part2)
    assert sol_part2 == 82301120
