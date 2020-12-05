import re
from functools import reduce
from typing import Tuple


def part1(raw_input: str) -> int:
    """
    >>> part1('''BFFFBBFRRR
    ... FFFBBBFRRR
    ... BBFFBBFRLL''')
    820
    """
    return max(map(get_seat_id, raw_input.split()))

def get_seat_id(boarding_pass: str) -> int:
    """
    >>> get_seat_id("BFFFBBFRRR")
    567
    >>> get_seat_id("FFFBBBFRRR")
    119
    >>> get_seat_id("BBFFBBFRLL")
    820
    """
    assert re.match(r"^[BFRL]{10}$", boarding_pass)
    return get_row(boarding_pass[:7], (0, 127)) * 8 + get_row(boarding_pass[7:], (0, 7))
    

def get_row(commands: str, interval: Tuple[int, int]) -> int:
    """
    >>> get_row("BFFFBBF", (0, 127))
    70
    >>> get_row("RLL", (0, 7))
    4
    """
    row = reduce(lambda i, c: partition_interval(c, *i), commands, interval)
    assert row[0] == row[1]
    return row[0]

def partition_interval(command: str, left: int, right: int) -> Tuple[int, int]:
    """
    >>> partition_interval("F", 0, 127)
    (0, 63)
    >>> partition_interval("B", 0, 63)
    (32, 63)
    >>> partition_interval("F", 44, 45)
    (44, 44)
    >>> partition_interval("B", 44, 45)
    (45, 45)
    >>> partition_interval("R", 0, 7)
    (4, 7)
    >>> partition_interval("L", 4, 7)
    (4, 5)
    """
    assert command in ["F", "B", "R", "L"]
    middle =  left + (right - left) / 2
    if command in ["F", "L"]:
        return left, int(middle)
    else:
        return int(middle) + 1, right


if __name__ == "__main__":
    with open("./data/day05.txt", "r") as f:
        data = f.read()
    
    print("PART 1")
    print(part1(data))

    print("PART2")
    all_seats = set(i for i in range(1024))
    all_used = set(map(get_seat_id, data.split()))
    all_free = all_seats - all_used
    right_seat = [x for x in all_free if (x-1) in all_used and (x+1) in all_used]
    assert len(right_seat) == 1
    print(right_seat[0])
