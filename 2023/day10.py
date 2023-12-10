import networkx as nx

def part1(input: str, replacement: str) -> int:
    """
    >>> part1('''.....
    ... .S-7.
    ... .|.|.
    ... .L-J.
    ... .....''', "F")
    4
    >>> part1('''-L|F7
    ... 7S-7|
    ... L|7||
    ... -L-J|
    ... L|-JF''', "F")
    4
    >>> part1('''..F7.
    ... .FJ|.
    ... SJ.L7
    ... |F--J
    ... LJ...''', "F")
    8
    >>> part1('''7-F7-
    ... .FJ|7
    ... SJLL7
    ... |F--J
    ... LJ.LJ''', "F")
    8
    """
    G, start = build_graph(input, replacement)
    return max(nx.single_source_shortest_path_length(G, start).values())//2

def part2(input: str, replacement: str) -> int:
    """
    >>> part2('''...........
    ... .S-------7.
    ... .|F-----7|.
    ... .||.....||.
    ... .||.....||.
    ... .|L-7.F-J|.
    ... .|..|.|..|.
    ... .L--J.L--J.
    ... ...........''', "F")
    4
    >>> part2('''...........
    ... .S------7.
    ... .|F----7|.
    ... .||....||.
    ... .||....||.
    ... .|L-7F-J|.
    ... .|..||..|.
    ... .L--JL--J.
    ... ..........''', "F")
    4
    """
    G, start = build_graph(input, replacement)
    print_connected(G, input)
    connected = [node for node in set.union(*(x for x in nx.connected_components(G) if (0,0) not in x and start not in x)) if node[0]%2==0 and node[1]%2==0]
    print(connected)
    return len(connected)

def build_graph(input, replacement):
    G = nx.Graph()
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                start = (2*x, 2*y)
                c = replacement
            if c == "-":
                G.add_edge((2*x, 2*y), (2*x + 1, 2*y))
                G.add_edge((2*x, 2*y), (2*x - 1, 2*y))
            if c == "|":
                G.add_edge((2*x, 2*y), (2*x, 2*y + 1))
                G.add_edge((2*x, 2*y), (2*x, 2*y - 1))
            if c == "7":
                G.add_edge((2*x, 2*y), (2*x, 2*y + 1))
                G.add_edge((2*x, 2*y), (2*x - 1, 2*y))
            if c == "J":
                G.add_edge((2*x, 2*y), (2*x, 2*y - 1))
                G.add_edge((2*x, 2*y), (2*x - 1, 2*y))
            if c == "L":    
                G.add_edge((2*x, 2*y), (2*x, 2*y - 1))
                G.add_edge((2*x, 2*y), (2*x + 1, 2*y))
            if c == "F":
                G.add_edge((2*x, 2*y), (2*x, 2*y + 1))
                G.add_edge((2*x, 2*y), (2*x + 1, 2*y))
            if c == ".":
                G.add_edge((2*x, 2*y), (2*x, 2*y + 1))
                G.add_edge((2*x, 2*y), (2*x + 1, 2*y))
                G.add_edge((2*x, 2*y), (2*x, 2*y - 1))
                G.add_edge((2*x, 2*y), (2*x - 1, 2*y))
    return G,start

def print_connected(G: nx.Graph, input: str) -> str:
    symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {node: symbols[i] for i, nodes in enumerate(nx.connected_components(G)) for node in nodes}
    lines = input.splitlines()
    n_y = len(lines)
    n_x = len(lines[0])
    for y in range(n_y):
        line = []
        for x in range(n_x):
            try:
                line.append(mapping[(2*x, 2*y)])
            except: 
                line.append(".")
        print("".join(line))


def print_dist(G: nx.Graph, input: str, start: tuple[int, int]) -> str:
    lines = input.splitlines()
    n_y = len(lines)
    n_x = len(lines[0])
    for y in range(n_y):
        line = []
        for x in range(n_x):
            try:
                line.append(str(nx.shortest_path_length(G, start, (2*x, 2*y))//2))
            except: 
                line.append(".")
        print("".join(line))


if __name__ == "__main__":
    with open("2023/data/day10.txt") as f:
        input = f.read()
    for replacement in "L":  #-|7JLF":
        p1 = part1(input, replacement)
        print(p1)
        assert p1 == 6812, "expected 6812, got {p1}"
    