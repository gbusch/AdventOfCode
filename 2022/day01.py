def parse_input(inp_str):
    """
    >>> inp_str = '''1000
    ... 2000
    ... 3000
    ...
    ... 4000'''
    >>> parse_input(inp_str)
    [[1000, 2000, 3000], [4000]]
    """
    return [[int(food) for food in elf.split("\n")] for elf in inp_str.split("\n\n")]


def total_calories(inp_list):
    """
    >>> inp_list = [[1000, 2000, 3000], [4000]]
    >>> total_calories(inp_list)
    [6000, 4000]
    """
    return [sum(elf) for elf in inp_list]


def most_calories(inp_list):
    """
    >>> inp_list = [[1000, 2000, 3000], [4000]]
    >>> most_calories(inp_list)
    6000
    """
    return max(total_calories(inp_list))


def top3_calories(inp_list):
    """
    >>> inp_list = [[1, 2, 3], [4], [5, 6], [7, 8, 9], [10]]
    >>> top3_calories(inp_list)
    45
    """
    return sum(sorted(total_calories(inp_list))[-3:])


if __name__ == "__main__":
    with open("data/day01.txt", "r") as f:
        inp_str = f.read()

    inp_list = parse_input(inp_str)

    print("part 1")
    print(most_calories(inp_list))

    print("part 2")
    print(top3_calories(inp_list))
