# thanks to the solution: https://github.com/matnad/aoc19/blob/master/day20/day20a.py
# good idea to practice NetworkX here!

from string import ascii_uppercase
import networkx as nx


def find_dims(data):
    return max(map(len, data)), len(data)


def get_grid(data, dims):
    grid = {}
    for x in range(dims[0]):
        for y in range(dims[1]):
            try:
                grid[(x, y)] = data[y][x] if data[y][x] != ' ' else '#'
            except IndexError:
                grid[(x, y)] = '#'
    return grid


def get_neighbours(point):
    """
    >>> get_neighbours((1, 1))
    [(0, 1), (2, 1), (1, 0), (1, 2)]
    """
    return [(point[0] + dx, point[1] + dy) for dx, dy in zip((-1, 1, 0, 0), (0, 0, -1, 1))]


def find_portals(grid, dims):
    from collections import defaultdict
    portals = defaultdict(list)
    for x in range(1, dims[0]-1):
        for y in range(1, dims[1]-1):
            symb = grid.get((x, y))
            if symb in ascii_uppercase:
                neighbours = [(a, b) for a, b in get_neighbours((x, y)) if grid.get((a, b)) != '#']
                if len(neighbours) == 2:
                    if grid.get(neighbours[0]) in ascii_uppercase:
                        letter, access = neighbours
                    else:
                        access, letter = neighbours
                    portal = ''.join(sorted([symb, grid.get(letter)]))
                    portals[portal].append(access)
    return portals


def generate_network(grid, dims, portals):
    G = nx.Graph()
    for x in range(1, dims[0]-1):
        for y in range(1, dims[1]-1):
            if grid.get((x, y)) == '.':
                G.add_node((x, y))
                neighbours = [(a, b) for a, b in get_neighbours((x, y)) if grid.get((a, b)) == '.']
                for n in neighbours:
                    G.add_edge((x, y), n)
    for portal, access_list in portals.items():
        if portal == 'AA':
            start = access_list[0]
        elif portal == 'ZZ':
            end = access_list[0]
        else:
            assert len(access_list) == 2
            G.add_edge(access_list[0], access_list[1])
    return G, start, end


def find_shortest_path_length(data_path):
    """
    >>> find_shortest_path_length('./data/day20a.txt')
    23
    >>> find_shortest_path_length('./data/day20b.txt')
    58
    """
    with open(data_path) as f:
        data = f.read().split("\n")

    dims = find_dims(data)
    grid = get_grid(data, dims)
    portals = find_portals(grid, dims)
    graph, start, end = generate_network(grid, dims, portals)
    return nx.shortest_path_length(graph, start, end)


print("PART ONE")
print(find_shortest_path_length('./data/day20.txt'))
