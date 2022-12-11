from dataclasses import dataclass
from typing import Dict, List
from itertools import zip_longest
from functools import reduce
import re


@dataclass
class Move:
    steps: int
    origin: int
    destination: int


def parse_setup(setup_input: str) -> Dict[int, List[str]]:
    """
    >>> setup_input = '''    [D]
    ... [N] [C]
    ... [Z] [M] [P]
    ...  1   2   3 '''
    >>> parse_setup(setup_input)
    {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}
    """
    return {
        i + 1: list(filter(lambda x: x != " ", stack))
        for i, stack in enumerate(
            zip_longest(
                *[
                    [crate for crate in stack[1::4].rstrip()]
                    for stack in setup_input.splitlines()[-2::-1]
                ],
                fillvalue=" "
            )
        )
    }


def parse_moves(move_line: str) -> Move:
    """
    >>> parse_moves("move 2 from 9 to 8")
    Move(steps=2, origin=9, destination=8)
    >>> parse_moves("move 13 from 4 to 2")
    Move(steps=13, origin=4, destination=2)
    """
    matches = re.match(r"move (\d+) from (\d+) to (\d+)", move_line)
    assert matches
    return Move(
        steps=int(matches.group(1)),
        origin=int(matches.group(2)),
        destination=int(matches.group(3)),
    )


def make_move(crates: Dict[int, List[str]], move: Move) -> Dict[int, List[str]]:
    """
    >>> make_move({1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}, Move(1, 2, 1))
    {1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}
    """
    crates[move.destination].append(crates[move.origin].pop())
    return crates


def make_moves(crates: Dict[int, List[str]], move: Move) -> Dict[int, List[str]]:
    """
    >>> make_moves({1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}, Move(3, 1, 3))
    {1: [], 2: ['M', 'C'], 3: ['P', 'D', 'N', 'Z']}
    """
    return reduce(lambda x, _: make_move(x, move), range(move.steps), crates)


def make_9001_move(crates: Dict[int, List[str]], move: Move) -> Dict[int, List[str]]:
    """
    >>> make_9001_move({1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}, Move(3, 1, 3))
    {1: [], 2: ['M', 'C'], 3: ['P', 'Z', 'N', 'D']}
    """
    crates[move.destination] += crates[move.origin][-move.steps :]
    crates[move.origin] = crates[move.origin][: -move.steps]
    return crates


def part1(input_setup: Dict[int, List[str]], moves: List[Move]) -> str:
    """
    >>> part1({1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}, [Move(1, 2, 1), Move(3, 1, 3), Move(2, 2, 1), Move(1, 1, 2)])
    'CMZ'
    """
    final_setup = reduce(lambda x, move: make_moves(x, move), moves, input_setup)
    return "".join(final_setup[i].pop() for i in range(1, max(final_setup.keys()) + 1))


def part2(input_setup: Dict[int, List[str]], moves: List[Move]) -> str:
    """
    >>> part2({1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}, [Move(1, 2, 1), Move(3, 1, 3), Move(2, 2, 1), Move(1, 1, 2)])
    'MCD'
    """
    final_setup = reduce(lambda x, move: make_9001_move(x, move), moves, input_setup)
    return "".join(
        final_setup[i].pop()
        for i in range(1, max(final_setup.keys()) + 1)
        if final_setup[i]
    )


if __name__ == "__main__":
    with open("data/day05.txt", "r") as f:
        inp_str = f.read()

    split_input = inp_str.split("\n\n")
    stacks = parse_setup(split_input[0])
    moves = list(map(parse_moves, split_input[1].splitlines()))

    print("part1")
    print(part1(stacks, moves))

    stacks = parse_setup(split_input[0])

    print("part2")
    print(part2(stacks, moves))
