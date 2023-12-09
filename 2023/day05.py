def part1(input: str) -> int:
    """Part 1
    >>> part1('''seeds: 79 14 55 13
    ...
    ... seed-to-soil map:
    ... 50 98 2
    ... 52 50 48
    ...
    ... soil-to-fertilizer map:
    ... 0 15 37
    ... 37 52 2
    ... 39 0 15
    ...
    ... fertilizer-to-water map:
    ... 49 53 8
    ... 0 11 42
    ... 42 0 7
    ... 57 7 4
    ...
    ... water-to-light map:
    ... 88 18 7
    ... 18 25 70
    ...
    ... light-to-temperature map:
    ... 45 77 23
    ... 81 45 19
    ... 68 64 13
    ...
    ... temperature-to-humidity map:
    ... 0 69 1
    ... 1 0 69
    ...
    ... humidity-to-location map:
    ... 60 56 37
    ... 56 93 4''')
    35
    """
    input_parts = input.split("\n\n")
    seeds = list(map(int, input_parts[0].split()[1:]))
    mappings = [m.split("\n", maxsplit=1)[1:][0] for m in input_parts[1:]]
    location = []
    for seed in seeds:
        for mapping in mappings:
            seed = mapping_func(seed, mapping)
        location.append(seed)
    return min(location)


def part2(input: str, step_size=1_000_000) -> int:
    """Part 2
    >>> part2('''seeds: 79 14 55 13
    ...
    ... seed-to-soil map:
    ... 50 98 2
    ... 52 50 48
    ...
    ... soil-to-fertilizer map:
    ... 0 15 37
    ... 37 52 2
    ... 39 0 15
    ...
    ... fertilizer-to-water map:
    ... 49 53 8
    ... 0 11 42
    ... 42 0 7
    ... 57 7 4
    ...
    ... water-to-light map:
    ... 88 18 7
    ... 18 25 70
    ...
    ... light-to-temperature map:
    ... 45 77 23
    ... 81 45 19
    ... 68 64 13
    ...
    ... temperature-to-humidity map:
    ... 0 69 1
    ... 1 0 69
    ...
    ... humidity-to-location map:
    ... 60 56 37
    ... 56 93 4''', step_size=3)
    46
    """

    def map_all(value: int, mappings: list) -> int:
        for mapping in mappings:
            value = mapping_func(value, mapping)
        return value

    input_parts = input.split("\n\n")
    seeds_raw = list(map(int, input_parts[0].split()[1:]))
    seeds = [
        (seeds_raw[2 * i], seeds_raw[2 * i + 1]) for i in range(len(seeds_raw) // 2)
    ]
    mappings = [m.split("\n", maxsplit=1)[1:][0] for m in input_parts[1:]]
    location = {
        (start, start + length, loc): map_all(loc, mappings)
        for start, length in seeds
        for loc in range(start, start + length, step_size)
    }
    (best_start, best_end, best_seed), _ = min(location.items(), key=lambda x: x[1])
    while step_size > 1:
        left_search = max(best_seed - step_size, best_start)
        right_search = min(best_seed + step_size, best_end)
        step_size = max(step_size // 10, 1)
        location_closer = {
            seed: map_all(seed, mappings)
            for seed in range(left_search, right_search, step_size)
        }
        best_seed, value = min(location_closer.items(), key=lambda x: x[1])
    return value


def mapping_func(value: int, input: str) -> int:
    """Returns a dict with the mapping of source to destination.
    >>> mapping_func(0, '''50 98 2
    ... 52 50 48''')
    0
    >>> mapping_func(99, '''50 98 2
    ... 52 50 48''')
    51
    >>> mapping_func(50, '''50 98 2
    ... 52 50 48''')
    52
    """
    for line in input.splitlines():
        dst_start, src_start, length = map(int, line.split())
        if src_start <= value < src_start + length:
            return value - src_start + dst_start
    return value


if __name__ == "__main__":
    with open("2023/data/day05.txt") as f:
        input = f.read()

    print(part1(input))
    print(part2(input))
