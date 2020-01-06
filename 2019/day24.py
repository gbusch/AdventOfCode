from collections import defaultdict


def parse_input(path):
    with open(path) as f:
        data = f.read().split()
    grid = defaultdict(lambda: '.')
    for y, line in enumerate(data):
        for x, state in enumerate(line):
            grid[(x, y)] = state
    return grid


def get_neighbours(position):
    """
    >>> get_neighbours((1,1))
    [(0, 1), (2, 1), (1, 0), (1, 2)]
    """
    return [(position[0] + dx, position[1] + dy) for dx, dy in zip((-1, 1, 0, 0), (0, 0, -1, 1))]


def new_state(grid):
    def new_state_field(position, grid):
        neighbouring_bugs = sum(map(lambda neighbour: grid[neighbour] == '#', get_neighbours(position)))
        if (grid[position] == '#') and (neighbouring_bugs != 1):
            return '.'
        elif (grid[position] == '.') and (neighbouring_bugs in [1, 2]):
            return '#'
        else:
            return grid[position]
    old_grid = grid.copy()
    return defaultdict(lambda: '.', {pos: new_state_field(pos, old_grid) for pos in grid})


def convert_to_list(grid):
    return tuple(grid[x, y] for y in range(5) for x in range(5))


def biodiversity_rating(grid_list):
    rating = 0
    for i, state in enumerate(grid_list):
        if state == '#':
            rating += pow(2, i)
    return rating


if __name__ == "__main__":
    grid = parse_input("./data/day24.txt")
    already_seen = set(grid)
    while True:
        grid = new_state(grid)
        grid_list = convert_to_list(grid)
        if grid_list in already_seen:
            break
        already_seen.add(grid_list)

    print("PART ONE")
    print(biodiversity_rating(convert_to_list(grid)))
