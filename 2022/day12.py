import networkx as nx
from typing import Dict, Tuple

EXAMPLE_INPUT = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def part1(G: nx.DiGraph) -> int:
    shortest = nx.shortest_path(G, start, destination)
    return len(shortest) - 1


def part2(G: nx.DiGraph) -> int:
    starting_positions = [pos for pos, height in height_map.items() if height == 0]
    all_shortest_paths = []
    for start_pos in starting_positions:
        try:
            all_shortest_paths.append(
                len(nx.shortest_path(G, start_pos, destination)) - 1
            )
        except nx.exception.NetworkXNoPath:
            pass
    return min(all_shortest_paths)


def generate_height_map(
    data: str,
) -> Tuple[Dict[Tuple[int, int], int], Tuple[int, int], Tuple[int, int]]:
    height_map = {}
    for y, row in enumerate(data.splitlines()):
        for x, pos in enumerate(row):
            height_map[(x, y)] = {"S": 0, "E": 25}.get(pos, ord(pos) - 97)
            if pos == "S":
                start = (x, y)
            if pos == "E":
                destination = (x, y)
    return height_map, start, destination


def generate_digraph(height_map: Dict[Tuple[int, int], int]) -> nx.DiGraph:
    G = nx.DiGraph()
    for x, y in height_map:
        if height_map.get((x + 1, y), 1000) - height_map[(x, y)] <= 1:
            G.add_edge((x, y), (x + 1, y))
        if height_map.get((x - 1, y), 1000) - height_map[(x, y)] <= 1:
            G.add_edge((x, y), (x - 1, y))
        if height_map.get((x, y + 1), 1000) - height_map[(x, y)] <= 1:
            G.add_edge((x, y), (x, y + 1))
        if height_map.get((x, y - 1), 1000) - height_map[(x, y)] <= 1:
            G.add_edge((x, y), (x, y - 1))
    return G


if __name__ == "__main__":
    height_map, start, destination = generate_height_map(EXAMPLE_INPUT)
    G = generate_digraph(height_map)
    assert part1(G) == 31
    assert part2(G) == 29

    with open("data/day12.txt", "r") as f:
        data = f.read()
    height_map, start, destination = generate_height_map(data)
    G = generate_digraph(height_map)
    print(f"part1: {part1(G)}")
    print(f"part2: {part2(G)}")
