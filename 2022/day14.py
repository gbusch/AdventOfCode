from typing import Set
from collections import namedtuple
from functools import reduce

Point = namedtuple("Point", "x y")


def add_rock_structure(inp_line: str) -> Set[Point]:
    """
    >>> sorted(add_rock_structure("498,4 -> 498,6 -> 496,6"))
    [Point(x=496, y=6), Point(x=497, y=6), Point(x=498, y=4), Point(x=498, y=5), Point(x=498, y=6)]
    """
    new_rock = set()
    corners = [Point(*map(int, p.split(","))) for p in inp_line.split(" -> ")]
    for i, corner in enumerate(corners[:-1]):
        next_corner = corners[i + 1]
        if corner.x == next_corner.x:
            y1, y2 = min(corner.y, next_corner.y), max(corner.y, next_corner.y)
            new_rock = new_rock.union(
                set(Point(corner.x, y) for y in range(y1, y2 + 1))
            )
        else:
            x1, x2 = min(corner.x, next_corner.x), max(corner.x, next_corner.x)
            new_rock = new_rock.union(
                set(Point(x, corner.y) for x in range(x1, x2 + 1))
            )
    return new_rock


def setup_world(inp_str: str) -> Set[Point]:
    """
    >>> sorted(setup_world('''498,4 -> 498,6 -> 496,6
    ... 503,4 -> 502,4'''))
    [Point(x=496, y=6), Point(x=497, y=6), Point(x=498, y=4), Point(x=498, y=5), Point(x=498, y=6), Point(x=502, y=4), Point(x=503, y=4)]
    """
    return reduce(
        lambda x, y: x.union(y), [add_rock_structure(l) for l in inp_str.splitlines()]
    )


def part1(inp_str):
    """
    >>> part1('''498,4 -> 498,6 -> 496,6
    ... 503,4 -> 502,4 -> 502,9 -> 494,9''')
    24
    """
    world = setup_world(inp_str)
    lower_border = max([w.y for w in world])
    no_sand = 0
    while True:
        sand = Point(500, 0)
        no_sand += 1
        while True:
            if sand.y >= lower_border:
                return no_sand - 1
            if (try_pos := Point(sand.x, sand.y + 1)) not in world:
                sand = try_pos
            elif (try_pos := Point(sand.x - 1, sand.y + 1)) not in world:
                sand = try_pos
            elif (try_pos := Point(sand.x + 1, sand.y + 1)) not in world:
                sand = try_pos
            else:
                world.add(sand)
                break


def part2(inp_str):
    """
    >>> part2('''498,4 -> 498,6 -> 496,6
    ... 503,4 -> 502,4 -> 502,9 -> 494,9''')
    93
    """
    world = setup_world(inp_str)
    lower_border = max([w.y for w in world]) + 2
    no_sand = 0
    while True:
        sand = Point(500, 0)
        no_sand += 1
        while True:
            if sand.y + 1 == lower_border:
                world.add(sand)
                break
            elif (try_pos := Point(sand.x, sand.y + 1)) not in world:
                sand = try_pos
            elif (try_pos := Point(sand.x - 1, sand.y + 1)) not in world:
                sand = try_pos
            elif (try_pos := Point(sand.x + 1, sand.y + 1)) not in world:
                sand = try_pos
            else:
                if sand.y == 0:
                    return no_sand
                world.add(sand)
                break


if __name__ == "__main__":
    EXAMPLE = """498,4 -> 498,6 -> 496,6
    503,4 -> 502,4 -> 502,9 -> 494,9"""
    assert part1(EXAMPLE) == 24

    with open("data/day14.txt", "r") as f:
        data = f.read()

    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")
