from day12 import *


class TestDay12:
    example_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    def test_1(self):
        height_map, start, destination = generate_height_map(self.example_input)
        G = generate_digraph(height_map)
        assert part1(G, start, destination) == 31

    def test_2(self):
        height_map, _, destination = generate_height_map(self.example_input)
        G = generate_digraph(height_map)
        assert part2(G, height_map, destination) == 29
