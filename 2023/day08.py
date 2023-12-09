from collections import namedtuple
import math

node = namedtuple("node", ["left", "right"])


def part1(input: str) -> int:
    """Part 1
    >>> part1('''RL
    ...
    ... AAA = (BBB, CCC)
    ... BBB = (DDD, EEE)
    ... CCC = (ZZZ, GGG)
    ... DDD = (DDD, DDD)
    ... EEE = (EEE, EEE)
    ... GGG = (GGG, GGG)
    ... ZZZ = (ZZZ, ZZZ)''')
    2
    >>> part1('''LLR
    ...
    ... AAA = (BBB, BBB)
    ... BBB = (AAA, ZZZ)
    ... ZZZ = (ZZZ, ZZZ)''')
    6
    """
    instructions, network = parse_input(input)
    i = 0
    start = "AAA"
    while True:
        start = move(start, instructions[i % len(instructions)], network)
        i += 1
        if start == "ZZZ":
            return i


def part2(input: str) -> int:
    """Part 2
    >>> part2('''LR
    ...
    ... 11A = (11B, XXX)
    ... 11B = (XXX, 11Z)
    ... 11Z = (11B, XXX)
    ... 22A = (22B, XXX)
    ... 22B = (22C, 22C)
    ... 22C = (22Z, 22Z)
    ... 22Z = (22B, 22B)
    ... XXX = (XXX, XXX)''')
    6
    """
    instructions, network = parse_input(input)
    steps = []
    for s in [s for s in network.keys() if s.endswith("A")]:
        i = 0
        while True:
            s = move(s, instructions[i % len(instructions)], network)
            i += 1
            if s.endswith("Z"):
                steps.append(i)
                break
    return math.lcm(*steps)


def parse_input(input: str):
    """Parse input
    >>> parse_input('''LLR
    ...
    ... AAA = (BBB, BBB)
    ... BBB = (AAA, ZZZ)
    ... ZZZ = (ZZZ, ZZZ)''')
    ('LLR', {'AAA': node(left='BBB', right='BBB'), 'BBB': node(left='AAA', right='ZZZ'), 'ZZZ': node(left='ZZZ', right='ZZZ')})
    """
    instructions = input.splitlines()[0]
    network = {}
    for line in input.splitlines()[2:]:
        node_name, node_value = line.split(" = ")
        network[node_name] = node(*node_value[1:-1].split(", "))
    return instructions, network


def move(start: str, direction: str, network: dict[str, node]) -> str:
    """Move according to instructions
    >>> move("AAA", "L", {"AAA": node("BBB", "CCC"), "BBB": node("DDD", "EEE")})
    'BBB'
    >>> move("BBB", "R", {"AAA": node("BBB", "CCC"), "BBB": node("DDD", "EEE")})
    'EEE'
    """
    return network[start].left if direction == "L" else network[start].right


if __name__ == "__main__":
    with open("2023/data/day08.txt") as file:
        input = file.read()
    print(part1(input))
    print(part2(input))
