from collections import defaultdict


def after_n_steps(n: int, state: dict[int, int]) -> int:
    """
    >>> after_n_steps(18, {1: 1, 2: 1, 3: 2, 4: 1})
    26
    >>> after_n_steps(80, {1: 1, 2: 1, 3: 2, 4: 1})
    5934
    >>> after_n_steps(256, {1: 1, 2: 1, 3: 2, 4: 1})
    26984457539
    """
    for _ in range(n):
        state = make_one_step(state)

    return sum(state.values())


def make_one_step(old_state: dict[int, int]) -> dict[int, int]:
    """
    >>> make_one_step({1: 1, 2: 1, 3: 2, 4: 1}) == {0: 1, 1: 1, 2: 2, 3: 1}
    True
    >>> make_one_step({0: 1, 1: 1, 2: 2, 3: 1}) == {0: 1, 1: 2, 2: 1, 6: 1, 8: 1}
    True
    >>> make_one_step({0: 2, 7: 1}) == {6: 3, 8: 2}
    True
    """
    new_state: dict[int, int] = defaultdict(int)
    for k, v in old_state.items():
        if k != 0:
            new_state[k - 1] += v
        else:
            new_state[6] += v
            new_state[8] += v
    return new_state


def convert_initial(inplist: list[int]) -> dict[int, int]:
    """
    >>> convert_initial([3, 4, 3, 1, 2]) == {1: 1, 2: 1, 3: 2, 4: 1}
    True
    """
    from collections import defaultdict

    counts: dict[int, int] = defaultdict(int)
    for i in inplist:
        counts[i] += 1
    return counts


if __name__ == "__main__":
    with open("data/day06.txt", "r") as f:
        inlist = [int(x) for x in f.read().split(",")]

    print(f"Part 1: {after_n_steps(80, convert_initial(inlist))}")
    print(f"Part 2: {after_n_steps(256, convert_initial(inlist))}")
