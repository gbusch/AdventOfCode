import numpy as np


def apply_pattern(position, length, base_pattern=[0, 1, 0, -1]):
    """
    >>> apply_pattern(0, 8)
    array([ 1,  0, -1,  0,  1,  0, -1,  0])
    >>> apply_pattern(2, 8)
    array([0, 0, 1, 1, 1, 0, 0, 0])
    """
    repeated = np.repeat(base_pattern, position+1)
    tiled = np.tile(repeated, length // len(repeated) + 1)
    return tiled[1:length+1]


def get_output_digit(input_signal, position):
    """
    >>> get_output_digit([1, 2, 3, 4, 5, 6, 7, 8], 0)
    4
    >>> get_output_digit([1, 2, 3, 4, 5, 6, 7, 8], 2)
    2
    """
    return int(str(np.sum(input_signal * apply_pattern(position, len(input_signal))))[-1])


def get_output_signal(input_signal):
    """
    >>> get_output_signal([1, 2, 3, 4, 5, 6, 7, 8])
    [4, 8, 2, 2, 6, 1, 5, 8]
    >>> get_output_signal([0, 3, 4, 1, 5, 5, 1, 8])
    [0, 1, 0, 2, 9, 4, 9, 8]
    """
    return [get_output_digit(input_signal, pos) for pos, _ in enumerate(input_signal)]


def first_eight_after_100(input_signal):
    """
    >>> first_eight_after_100('80871224585914546619083218645595')
    24176176
    >>> first_eight_after_100('19617804207202209144916044189917')
    73745418
    >>> first_eight_after_100('69317163492948606335995924319873')
    52432133
    """
    signal = [int(i) for i in input_signal]
    for i in range(100):
        signal = get_output_signal(signal)
    return int("".join(str(s) for s in signal[:8]))


def part_2(input_signal):
    """
    >>> part_2('03036732577212944063491565474664')
    84462026
    >>> part_2('02935109699940807407585447034323')
    78725270
    >>> part_2('03081770884921959731165446850517')
    53553731
    """
    offset = int(input_signal[:7])
    full_input = np.tile([int(i) for i in input_signal], 10000)
    signal = full_input[offset:]
    assert offset > len(signal) / 2
    for _ in range(100):
        for i in range(-2, -len(signal)-1, -1):
            signal[i] = (signal[i] + signal[i+1]) % 10
    return int("".join(str(s) for s in signal[:8]))


if __name__ == "__main__":
    with open("./data/day16.txt") as f:
        data = f.read()

    print("PART ONE")
    part1 = first_eight_after_100(data)
    print(part1)
    assert part1 == 45834272

    print("PART TWO")
    part2 = part_2(data)
    print(part2)
    assert part2 == 37615297
