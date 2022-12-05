from typing import Dict, List
from itertools import zip_longest
from functools import reduce
import re


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


def parse_moves(move_line: str):
    """
    >>> parse_moves("move 2 from 9 to 8")
    (2, 9, 8)
    >>> parse_moves("move 13 from 4 to 2")
    (13, 4, 2)
    """
    matches = re.match(r"move (\d+) from (\d+) to (\d+)", move_line)
    return tuple(int(matches.group(x)) for x in range(1, 4))


def make_move(crates, move):
    """
    >>> make_move({1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}, (2, 1))
    {1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}
    """
    crates[move[1]].append(crates[move[0]].pop())
    return crates


def make_moves(crates, move):
    """
    >>> make_moves({1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}, (3, 1, 3))
    {1: [], 2: ['M', 'C'], 3: ['P', 'D', 'N', 'Z']}
    """
    return reduce(lambda x, _: make_move(x, (move[1], move[2])), range(move[0]), crates)


def part1(input_setup, moves):
    """
    >>> part1({1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}, [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)])
    'CMZ'
    """
    final_setup = reduce(lambda x, move: make_moves(x, move), moves, input_setup)
    return "".join(final_setup[i].pop() for i in range(1, max(final_setup.keys())+1))


if __name__ == "__main__":
    with open("data/day05.txt", "r") as f:
        inp_str = f.read()
    
    split_input = inp_str.split("\n\n")
    stacks = parse_setup(split_input[0])
    moves = list(map(parse_moves, split_input[1].splitlines()))

    print("part1")
    print(part1(stacks, moves))

