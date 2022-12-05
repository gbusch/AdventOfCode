from typing import List, Tuple, Dict


RULES: Dict[Tuple[str, str], str] = {
    ("A", "X"): "Y",
    ("B", "Y"): "Y",
    ("C", "Z"): "Y",
    ("A", "Y"): "Z",
    ("B", "Z"): "Z",
    ("C", "X"): "Z",
    ("A", "Z"): "X",
    ("B", "X"): "X",
    ("C", "Y"): "X",
}

RESULT_POINTS: Dict[str, int] = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

BASE_POINTS: Dict[str, int] = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def parse_input(inp_str: str) -> List[Tuple[str, str]]:
    """
    >>> inp_str = '''A Y
    ... B X
    ... C Z'''
    >>> parse_input(inp_str)
    [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
    """
    return [tuple(round.split(maxsplit=1)) for round in inp_str.splitlines()]

def score_round(round: Tuple[str, str]) -> int:
    """
    >>> score_round(("A", "Y"))
    8
    >>> score_round(("B", "X"))
    1
    >>> score_round(("C", "Z"))
    6
    """
    return RESULT_POINTS[RULES[round]] + BASE_POINTS[round[1]]


def make_choice(opponent: str, result: str) -> str:
    """
    >>> make_choice("A", "Y")
    'X'
    >>> make_choice("B", "X")
    'X'
    >>> make_choice("C", "Z")
    'X'
    """
    choice_map = {
        (opponent, result): choice 
        for (opponent, choice), result 
        in RULES.items()
    }
    return choice_map[(opponent, result)]


def part2(rounds: List[Tuple[str, str]]) -> int:
    """
    >>> part2([("A", "Y"), ("B", "X"), ("C", "Z")])
    12
    """
    return sum([score_round((round[0], make_choice(*round))) for round in rounds])


def score_total(rounds: List[Tuple[str, str]]) -> int:
    """
    >>> score_total([("A", "Y"), ("B", "X"), ("C", "Z")])
    15
    """
    return sum([score_round(round) for round in rounds])


if __name__ == "__main__":
    with open("data/day02.txt", "r") as f:
        inp_str = f.read()

    rounds = parse_input(inp_str)

    print("part 1")
    print(score_total(rounds))

    print("part 2")
    print(part2(rounds))
