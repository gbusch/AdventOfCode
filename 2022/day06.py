def find_marker(datastream: str, distinct_no: int) -> int:
    """
    >>> find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4)
    7
    >>> find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)
    5
    >>> find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)
    11
    >>> find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)
    19
    >>> find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)
    29
    """
    for i in range(len(datastream) - distinct_no + 1):
        marker = datastream[i : i + distinct_no]
        if len(marker) == len(set(marker)):
            return i + distinct_no
    return -1


if __name__ == "__main__":
    with open("data/day06.txt", "r") as f:
        inp_str = f.read()

    print("part 1")
    print(find_marker(inp_str, 4))

    print("part 2")
    print(find_marker(inp_str, 14))
