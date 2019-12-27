from collections import deque


def deal_into_new_stack(pos, stack_len):
    """
    >>> list(map(lambda x: deal_into_new_stack(x, 10), range(10)))
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    """
    return (stack_len - 1) - pos


def cut_N_cards(pos, N, stack_len):
    """
    >>> list(map(lambda x: cut_N_cards(x, 3, 10), range(10)))
    [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
    >>> list(map(lambda x: cut_N_cards(x, -4, 10), range(10)))
    [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
    """
    return (pos - N) % stack_len


def deal_with_increment_N(pos, N, stack_len):
    """
    >>> list(map(lambda x: deal_with_increment_N(x, 3, 10), range(10)))
    [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
    """
    return (pos * N) % stack_len


def apply_shuffling_technique(pos, command, stack_len):
    """
    >>> list(map(lambda x: apply_shuffling_technique(x, "deal into new stack", 10), range(10)))
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> list(map(lambda x: apply_shuffling_technique(x, "cut 3", 10), range(10)))
    [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
    >>> list(map(lambda x: apply_shuffling_technique(x, "cut -4", 10), range(10)))
    [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
    >>> list(map(lambda x: apply_shuffling_technique(x, "deal with increment 3", 10), range(10)))
    [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
    """
    if "deal into new stack" in command:
        return deal_into_new_stack(pos, stack_len)
    if "cut" in command:
        return cut_N_cards(pos, int(command.split()[-1]), stack_len)
    if "deal with increment" in command:
        return deal_with_increment_N(pos, int(command.split()[-1]), stack_len)


def apply_shuffling_sequence(pos, commands, stack_len):
    """
    >>> list(map(lambda x: apply_shuffling_sequence(x, ["deal with increment 7", "deal into new stack", "deal into new stack"], 10), range(10)))
    [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
    >>> list(map(lambda x: apply_shuffling_sequence(x, ["cut 6", "deal with increment 7", "deal into new stack"], 10), range(10)))
    [1, 4, 7, 0, 3, 6, 9, 2, 5, 8]
    >>> list(map(lambda x: apply_shuffling_sequence(x, ["deal with increment 7", "deal with increment 9", "cut -2"], 10), range(10)))
    [2, 5, 8, 1, 4, 7, 0, 3, 6, 9]
    >>> list(map(lambda x: apply_shuffling_sequence(x, ["deal into new stack", "cut -2", "deal with increment 7", "cut 8",
    ...   "cut -4", "deal with increment 7", "cut 3", "deal with increment 9", "deal with increment 3", "cut -1"], 10), range(10)))
    [7, 4, 1, 8, 5, 2, 9, 6, 3, 0]
    """
    for command in commands:
        pos = apply_shuffling_technique(pos, command, stack_len)
    return pos


if __name__ == "__main__":
    with open("./data/day22.txt") as f:
        commands = f.read().split("\n")

    print("PART ONE")
    new_pos = apply_shuffling_sequence(2019, commands, 10007)
    assert new_pos == 4485
    print(new_pos)

    print("PART TWO")
    pos = 2020
    for _ in range(101741582076661):
        pos = apply_shuffling_sequence(pos, commands, 119315717514047)
    print(pos)
