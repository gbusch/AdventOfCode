from typing import List
from nptyping import NDArray
import numpy as np

EXAMPLE_INPUT = """30373
25512
65332
33549
35390"""


def is_visible(trees: List[int]) -> List[int]:
    highest = -1
    tree_list = []
    for tree in trees:
        if tree > highest:
            tree_list.append(1)
            highest = tree
        else:
            tree_list.append(0)
    return tree_list


def is_shorter(trees: List[int], center: int) -> List:
    tree_list = []
    for tree in trees:
        if tree < center:
            tree_list.append(1)
        else:
            tree_list.append(1)
            break
    return tree_list


def visible_tree_map(arr):
    from_left = np.zeros(arr.shape)
    for y in range(arr.shape[0]):
        from_left[y, :] = is_visible(arr[y, :])

    from_top = np.zeros(arr.shape)
    for x in range(arr.shape[1]):
        from_top[:, x] = is_visible(arr[:, x])

    from_right = np.zeros(arr.shape)
    for y in range(arr.shape[0]):
        from_right[y, :] = is_visible(arr[y, :][::-1])[::-1]

    from_bottom = np.zeros(arr.shape)
    for x in range(arr.shape[1]):
        from_bottom[:, x] = is_visible(arr[:, x][::-1])[::-1]

    return from_left + from_right + from_bottom + from_top


def get_scenic_score(input_map, x, y):
    right = is_shorter(input_map[x, y + 1 :], input_map[x, y])
    left = is_shorter(input_map[x, :y][::-1], input_map[x, y])
    bottom = is_shorter(input_map[x + 1 :, y], input_map[x, y])
    top = is_shorter(input_map[:x, y][::-1], input_map[x, y])
    return sum(right) * sum(left) * sum(bottom) * sum(top)


def get_highest_scenic_score(input_map):
    score = 0
    for y in range(input_map.shape[1]):
        for x in range(input_map.shape[0]):
            if (new_score := get_scenic_score(input_map, x, y)) > score:
                score = new_score
    return score


def parse_map(input_string: str):
    return np.array([[int(x) for x in line] for line in input_string.splitlines()])


if __name__ == "__main__":
    assert sum(sum(visible_tree_map(parse_map(EXAMPLE_INPUT)) > 0)) == 21

    assert get_scenic_score(parse_map(EXAMPLE_INPUT), 1, 2) == 4
    assert get_scenic_score(parse_map(EXAMPLE_INPUT), 3, 2) == 8
    assert get_highest_scenic_score(parse_map(EXAMPLE_INPUT)) == 8

    with open("data/day08.txt", "r") as f:
        input_string = f.read()

    print("part1")
    input_map = parse_map(input_string)
    visible_trees = visible_tree_map(input_map) > 0
    print(sum(sum(visible_tree_map(input_map) > 0)))

    print("part2")
    print(get_highest_scenic_score(input_map))
