from collections import defaultdict
from itertools import accumulate


EXAMPLE_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

EXAMPLE_INPUT2 = """$ cd /
$ ls
dir a
14848514 b.txt
$ cd a
$ ls
dir e
$ cd e
$ ls
500 i"""


def cumulative_dir_sizes(input):
    current_dir = []
    dir_sizes = defaultdict(int)

    for line in input.splitlines():
        match line.split():
            case "$", "cd", "/":
                current_dir = ["/"]
            case "$", "cd", "..":
                current_dir.pop()
            case "$", "cd", d:
                current_dir.append(f"/{d}")
            case ("$", "ls") | ("dir", _):
                pass
            case file_size, _:
                for parent in accumulate(current_dir):
                    dir_sizes[parent] += int(file_size)
    return dir_sizes


def part1(cumulative_sizes):
    return sum(filter(lambda val: val <= 100_000, cumulative_sizes.values()))


def part2(cumulative_sizes):
    required_saving = cumulative_sizes["/"] - 40_000_000
    return sorted(
        filter(lambda val: val >= required_saving, cumulative_sizes.values())
    )[0]


if __name__ == "__main__":
    cum_sizes = cumulative_dir_sizes(EXAMPLE_INPUT)
    assert part1(cum_sizes) == 95437
    assert part2(cum_sizes) == 24933642

    cum_sizes2 = cumulative_dir_sizes(EXAMPLE_INPUT2)
    assert part1(cum_sizes2) == 1000

    with open("data/day07.txt", "r") as f:
        inp_str = f.read()

    cum_sizes_inp = cumulative_dir_sizes(inp_str)

    solution1 = part1(cum_sizes_inp)
    assert solution1 == 1915606
    print(f"part1: {solution1}")

    solution2 = part2(cum_sizes_inp)
    assert solution2 == 5025657
    print(f"part2: {solution2}")
