import re


def part1(inp: str) -> int:
    """
    >>> part1('mul(44,46)')
    2024
    >>> part1('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))')
    161
    """
    return sum(
        int(x[0]) * int(x[1]) for x in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp)
    )


def part2(inp: str) -> int:
    """
    >>> part2('''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))''')
    48
    """
    do = True
    sum = 0
    for m in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", inp):
        if m[3] == "don't":
            do = False
            continue
        if m[2] == "do":
            do = True
            continue
        if do:
            sum += int(m[0]) * int(m[1])
    return sum


if __name__ == "__main__":
    with open("2024/data/day03.txt", "r") as f:
        data = f.read()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
