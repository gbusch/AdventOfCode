from collections import namedtuple

Position = namedtuple("Position", "x y")


def make_motions(commands: str, no_knots: int) -> int:
    """
    >>> make_motions('''R 4
    ... U 4
    ... L 3
    ... D 1
    ... R 4
    ... D 1
    ... L 5
    ... R 2''', 2)
    13
    >>> make_motions('''R 4
    ... U 4
    ... L 3
    ... D 1
    ... R 4
    ... D 1
    ... L 5
    ... R 2''', 10)
    1
    >>> make_motions('''R 5
    ... U 8
    ... L 8
    ... D 3
    ... R 17
    ... D 10
    ... L 25
    ... U 20''', 10)
    36
    """
    knots = [Position(1, 1) for _ in range(no_knots)]

    tail_pos = set()

    for line in commands.splitlines():
        direction, times = line.strip().split(" ")
        for _ in range(int(times)):
            knots[0] = move_head(knots[0], direction)
            for k in range(1, no_knots):
                knots[k] = move_tail(knots[k], knots[k - 1])
            tail_pos.add(knots[no_knots - 1])
    return len(tail_pos)


def move_head(pos: Position, direction) -> Position:
    """
    >>> move_head(Position(1, 1), "R")
    Position(x=2, y=1)
    >>> move_head(Position(2, 2), "R")
    Position(x=3, y=2)
    >>> move_head(Position(1, 1), "D")
    Position(x=1, y=0)
    >>> move_head(Position(1, 1), "L")
    Position(x=0, y=1)
    >>> move_head(Position(1, 1), "U")
    Position(x=1, y=2)
    """
    match direction:
        case "R":
            new_pos = Position(pos.x + 1, pos.y)
        case "L":
            new_pos = Position(pos.x - 1, pos.y)
        case "U":
            new_pos = Position(pos.x, pos.y + 1)
        case "D":
            new_pos = Position(pos.x, pos.y - 1)
    return new_pos


def move_tail(tail: Position, head: Position) -> Position:
    """
    >>> move_tail(Position(1, 1), Position(2, 1))
    Position(x=1, y=1)
    >>> move_tail(Position(2, 1), Position(1, 2))
    Position(x=2, y=1)
    >>> move_tail(Position(1, 1), Position(1, 1))
    Position(x=1, y=1)
    >>> move_tail(Position(1, 1), Position(3, 1))
    Position(x=2, y=1)
    >>> move_tail(Position(3, 1), Position(1, 1))
    Position(x=2, y=1)
    >>> move_tail(Position(1, 3), Position(1, 1))
    Position(x=1, y=2)
    >>> move_tail(Position(1, 1), Position(1, 3))
    Position(x=1, y=2)
    >>> move_tail(Position(1, 1), Position(2, 3))
    Position(x=2, y=2)
    >>> move_tail(Position(1, 1), Position(3, 2))
    Position(x=2, y=2)
    >>> move_tail(Position(2, 3), Position(1, 1))
    Position(x=1, y=2)
    >>> move_tail(Position(3, 2), Position(1, 1))
    Position(x=2, y=1)
    """
    if (tail.x - head.x) ** 2 <= 1 and (tail.y - head.y) ** 2 <= 1:
        return Position(tail.x, tail.y)
    elif (tail.x == head.x) and abs(tail.y - head.y) == 2:
        return Position(tail.x, tail.y + (head.y - tail.y) // 2)
    elif abs(tail.x - head.x) == 2 and (tail.y == head.y):
        return Position(tail.x + (head.x - tail.x) // 2, tail.y)
    else:
        return Position(tail.x + sign(head.x - tail.x), tail.y + sign(head.y - tail.y))


def sign(num: float) -> int:
    """
    >>> sign(-0.5)
    -1
    >>> sign(0.5)
    1
    """
    return 1 if num > 0 else -1


if __name__ == "__main__":
    with open("data/day09.txt", "r") as f:
        inp_str = f.read()

    print("part1")
    print(make_motions(inp_str, 2))
    print("part2")
    print(make_motions(inp_str, 10))
