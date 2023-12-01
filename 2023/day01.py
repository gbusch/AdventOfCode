import re

from typing import Iterator


def part1(string: str) -> int:
    """
    >>> part1('''1abc2
    ... pqr3stu8vwx
    ... a1b2c3d4e5f
    ... treb7uchet''')
    142
    """
    return sum(
        int(d[0] + d[-1]) for d in [find_digits(line) for line in string.splitlines()]
    )


def part2(string: str) -> int:
    """
    >>> part2('''two1nine
    ... eightwothree
    ... abcone2threexyz
    ... xtwone3four
    ... 4nineeightseven2
    ... zoneight234
    ... 7pqrstsixteen''')
    281
    """
    return sum(
        int(d[0] + d[-1])
        for d in [
            list(replace_spelled_out_numbers(line)) for line in string.splitlines()
        ]
    )


def replace_spelled_out_numbers(string: str) -> Iterator[str]:
    """
    Replace spelled out numbers with digits
    >>> list(replace_spelled_out_numbers("two1nine"))
    ['2', '1', '9']
    >>> list(replace_spelled_out_numbers("eightwothree"))
    ['8', '2', '3']
    >>> list(replace_spelled_out_numbers("7pqrstsixteen"))
    ['7', '6']
    """
    number_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for i in range(len(string)):
        if string[i].isdigit():
            yield string[i]
        for spelled, number in number_mapping.items():
            if spelled in string[i + 1 - len(spelled) : i + 1]:
                yield number


def find_digits(string: str) -> list[str]:
    """
    Find all digits in a string and return them as a list
    >>> find_digits("a1b2c3d4e5f")
    ['1', '2', '3', '4', '5']
    >>> find_digits("1abc2")
    ['1', '2']
    """
    digits = re.findall(r"\d", string)
    return digits


if __name__ == "__main__":
    with open("2023/data/day01.txt", "r") as f:
        contents = f.read()
    print(part1(contents))
    print(part2(contents))
