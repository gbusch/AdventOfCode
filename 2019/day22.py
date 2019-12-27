from collections import deque


def deal_into_new_stack(stack):
    """
    >>> deal_into_new_stack(deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    """
    old_stack = stack.copy()
    new_stack = deque()
    while old_stack:
        new_stack.append(old_stack.pop())
    return new_stack


def cut_N_cards(stack, N):
    """
    >>> cut_N_cards(deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 3)
    deque([3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
    >>> cut_N_cards(deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), -4)
    deque([6, 7, 8, 9, 0, 1, 2, 3, 4, 5])
    """
    old_stack = stack.copy()
    new_stack = deque()
    if N >= 0:
        for n in range(N):
            new_stack.append(old_stack.popleft())
        while old_stack:
            new_stack.appendleft(old_stack.pop())
    else:
        for n in range(-N):
            new_stack.appendleft(old_stack.pop())
        while old_stack:
            new_stack.append(old_stack.popleft())
    return new_stack


def deal_with_increment_N(stack, N):
    """
    >>> deal_with_increment_N(deque(range(10)), 3)
    deque([0, 7, 4, 1, 8, 5, 2, 9, 6, 3])
    >>> deal_with_increment_N(deque(range(10)), 7)
    deque([0, 3, 6, 9, 2, 5, 8, 1, 4, 7])
    >>> deal_with_increment_N(deque(range(10)), 9)
    deque([0, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    """
    old_stack = stack.copy()
    new_stack = dict()
    i = 0
    while old_stack:
        new_stack[i] = old_stack.popleft()
        i = (i+N) % len(stack)
    return deque([new_stack[i] for i in range(len(stack))])


def apply_shuffling_technique(stack, command):
    """
    >>> apply_shuffling_technique(deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), "deal into new stack")
    deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    >>> apply_shuffling_technique(deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), "cut 3")
    deque([3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
    >>> apply_shuffling_technique(deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), "cut -4")
    deque([6, 7, 8, 9, 0, 1, 2, 3, 4, 5])
    >>> apply_shuffling_technique(deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), "deal with increment 3")
    deque([0, 7, 4, 1, 8, 5, 2, 9, 6, 3])
    """
    if "deal into new stack" in command:
        return deal_into_new_stack(stack)
    if "cut" in command:
        return cut_N_cards(stack, int(command.split()[-1]))
    if "deal with increment" in command:
        return deal_with_increment_N(stack, int(command.split()[-1]))


def apply_shuffling_sequence(stack, commands):
    """
    >>> stack = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> apply_shuffling_sequence(stack, ["deal with increment 7", "deal into new stack", "deal into new stack"])
    deque([0, 3, 6, 9, 2, 5, 8, 1, 4, 7])
    >>> apply_shuffling_sequence(stack, ["cut 6", "deal with increment 7", "deal into new stack"])
    deque([3, 0, 7, 4, 1, 8, 5, 2, 9, 6])
    >>> apply_shuffling_sequence(stack, ["deal with increment 7", "deal with increment 9", "cut -2"])
    deque([6, 3, 0, 7, 4, 1, 8, 5, 2, 9])
    >>> apply_shuffling_sequence(stack, ["deal into new stack", "cut -2", "deal with increment 7", "cut 8",
    ...   "cut -4", "deal with increment 7", "cut 3", "deal with increment 9", "deal with increment 3", "cut -1"])
    deque([9, 2, 5, 8, 1, 4, 7, 0, 3, 6])
    """
    from functools import reduce
    return reduce(lambda s, c: apply_shuffling_technique(s, c), commands, stack)


if __name__ == "__main__":
    with open("./data/day22.txt") as f:
        commands = f.read().split("\n")

    print("PART ONE")
    new_stack = apply_shuffling_sequence(deque(range(10007)), commands)
    print(new_stack.index(2019))

    # too slow for part two
