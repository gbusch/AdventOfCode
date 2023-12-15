import numpy as np
from itertools import combinations


def main(input: str, factor: int = 2) -> int:
    """
    >>> main('''...#......
    ... .......#..
    ... #.........
    ... ..........
    ... ......#...
    ... .#........
    ... .........#
    ... ..........
    ... .......#..
    ... #...#.....''')
    374
    >>> main('''...#......
    ... .......#..
    ... #.........
    ... ..........
    ... ......#...
    ... .#........
    ... .........#
    ... ..........
    ... .......#..
    ... #...#.....''', factor=10)
    1030
    >>> main('''...#......
    ... .......#..
    ... #.........
    ... ..........
    ... ......#...
    ... .#........
    ... .........#
    ... ..........
    ... .......#..
    ... #...#.....''', factor=100)
    8410
    """
    grid = np.array([list(line) for line in input.splitlines()])
    asteroids = np.argwhere(grid == "#")
    grid_expand_row = []
    for r, row in enumerate(grid):
        if np.all(row == "."):
            grid_expand_row.append(r)
    grid_expand_col = []
    for c, col in enumerate(grid.T):
        if np.all(col == "."):
            grid_expand_col.append(c)
    asteroids_expand = [
        apply_expansion(a, grid_expand_row, grid_expand_col, factor) for a in asteroids
    ]
    return sum(manhattan(*c) for c in combinations(asteroids_expand, 2))


def apply_expansion(
    asteroid: tuple[int, int],
    expand_rows: list[int],
    expand_cols: list[int],
    factor: int = 2,
) -> tuple[int, int]:
    """
    >>> apply_expansion((0, 3), [1, 2], [1, 2])
    (0, 5)
    >>> apply_expansion((3, 1), [2, 4], [2, 4])
    (4, 1)
    >>> apply_expansion((3, 1), [2, 4], [2, 4], factor=10)
    (12, 1)
    """
    asteroid_row, asteroid_col = asteroid
    asteroid_row += sum(factor - 1 for r in expand_rows if r < asteroid_row)
    asteroid_col += sum(factor - 1 for c in expand_cols if c < asteroid_col)
    return asteroid_row, asteroid_col


def manhattan(a: tuple[int, int], b: tuple[int, int]) -> int:
    """
    >>> manhattan((0, 0), (1, 1))
    2
    >>> manhattan((0, 0), (-1, 1))
    2
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == "__main__":
    with open("2023/data/day11.txt", "r") as f:
        input = f.read()
    p1 = main(input)
    assert p1 == 10885634
    print(f"Part 1: {p1}")
    p2 = main(input, factor=1000000)
    print(f"Part 1: {p2}")
