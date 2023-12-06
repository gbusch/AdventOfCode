def part1(input: str) -> int:
    """Part 1
    >>> part1('''Time:      7  15   30
    ... Distance:  9  40  200''')
    288
    """
    times_raw, distances_raw = input.split("\n")
    times = [int(time) for time in times_raw.split()[1:]]
    distances = [int(distance) for distance in distances_raw.split()[1:]]
    result = 1
    for t, d in zip(times, distances):
        result *= win_possibilities(t, d)
    return result


def part2(input: str) -> int:
    """Part 2
    >>> part2('''Time:      7  15   30
    ... Distance:  9  40  200''')
    71503
    """
    times_raw, distances_raw = input.split("\n")
    times = int("".join(times_raw.split()[1:]))
    distances = int("".join(distances_raw.split()[1:]))
    return win_possibilities(times, distances)


def win_possibilities(time: int, distance: int) -> int:
    """Win possibilities depending on time and distance
    >>> win_possibilities(7, 9)
    4
    >>> win_possibilities(30, 200)
    9
    """
    for button in range(time + 1):
        if travel_distance(button, time) > distance:
            first_win = button
            break
    for button in range(time + 1)[::-1]:
        if travel_distance(button, time) > distance:
            last_win = button
            break
    return last_win - first_win + 1


def travel_distance(button: int, time: int) -> int:
    """Travel distance depending on button time
    >>> travel_distance(0, 7)
    0
    >>> travel_distance(1, 7)
    6
    >>> travel_distance(2, 7)
    10
    >>> travel_distance(3, 7)
    12
    >>> travel_distance(7, 7)
    0
    >>> travel_distance(8, 7)
    -1
    """
    if button < 0 or button > time:
        return -1
    return (time - button) * button


if __name__ == "__main__":
    with open("2023/data/day06.txt", "r") as f:
        input = f.read()
    print(part1(input))
    print(part2(input))
