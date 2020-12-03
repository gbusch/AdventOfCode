def walk(input_map, steps):
    """
    >>> walk('''..##.......
    ... #...#...#..
    ... .#....#..#.
    ... ..#.#...#.#
    ... .#...##..#.
    ... ..#.##.....
    ... .#.#.#....#
    ... .#........#
    ... #.##...#...
    ... #...##....#
    ... .#..#...#.#''', (3, 1))
    7
    """
    height, width, trees = parse_map(input_map)
    coord = (0, 0)
    n_trees = 0
    while (coord[1] < height):
        if coord in trees: n_trees += 1
        coord = ((coord[0] + steps[0]) % width, coord[1] + steps[1])
    return n_trees


def multiple_walks(input_map):
    """
    >>> multiple_walks('''..##.......
    ... #...#...#..
    ... .#....#..#.
    ... ..#.#...#.#
    ... .#...##..#.
    ... ..#.##.....
    ... .#.#.#....#
    ... .#........#
    ... #.##...#...
    ... #...##....#
    ... .#..#...#.#''')
    336
    """
    m_steps = 1
    for steps in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        m_steps *= walk(input_map, steps)
    return m_steps


def parse_map(input_map):
    """
    >>> parse_map('''..
    ... #.''')
    (2, 2, set([(0, 1)]))
    """
    rows = input_map.splitlines()
    parsed = set()
    for y, row in enumerate(rows):
        for x, point in enumerate(row):
            if point == '#':
                parsed.add((x, y))
    return len(rows), len(rows[0]), parsed


if __name__ == "__main__":
    with open("./data/day03.txt", "r") as f:
        input_map = f.read()
    
    print("PART 1")
    print(walk(input_map, (3, 1)))

    print("PART 2")
    print(multiple_walks(input_map))
