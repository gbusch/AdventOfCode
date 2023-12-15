from collections import OrderedDict, defaultdict


def part1(input: str) -> int:
    """
    >>> part1("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")
    1320
    """
    return sum(run_hash(s) for s in input.split(","))


def part2(input: str) -> int:
    """
    >>> part2("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")
    145
    """
    contents: dict[int, dict[str, int]] = defaultdict(OrderedDict)
    for s in input.split(","):
        if "=" in s:
            lense, focus = s.split("=")
            box = run_hash(lense)
            contents[box][lense] = int(focus)
        else:
            lense = s[:-1]
            box = run_hash(lense)
            try:
                del contents[box][lense]
            except:
                ...
    return sum(
        (b + 1) * (s + 1) * focus
        for b, box in contents.items()
        for s, (_, focus) in enumerate(box.items())
    )


def run_hash(input: str) -> int:
    """
    >>> run_hash("HASH")
    52
    >>> run_hash("rn=1")
    30
    >>> run_hash("cm-")
    253
    >>> run_hash("ot=7")
    231
    """
    current = 0
    for s in input:
        current = ((current + ord(s)) * 17) % 256
    return current


if __name__ == "__main__":
    with open("2023/data/day15.txt") as f:
        data = f.read().strip()

    print(part1(data))
    print(part2(data))
