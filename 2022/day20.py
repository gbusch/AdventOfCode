from typing import List


def move_list(inp_list: List[int], moves: int) -> List[int]:
    """
    >>> move_list([1, 2, -3, 3, -2, 0, 4], 1)
    [2, 1, -3, 3, -2, 0, 4]
    >>> move_list([1, 2, -3, 3, -2, 0, 4], 2)
    [1, -3, 2, 3, -2, 0, 4]
    >>> move_list([1, 2, -3, 3, -2, 0, 4], 3)
    [1, 2, 3, -2, -3, 0, 4]
    >>> move_list([1, 2, -3, 3, -2, 0, 4], 4)
    [1, 2, -2, -3, 0, 3, 4]
    >>> move_list([1, 2, -3, 3, -2, 0, 4], 5)
    [1, 2, -3, 0, 3, 4, -2]
    >>> move_list([1, 2, -3, 3, -2, 0, 4], 6)
    [1, 2, -3, 0, 3, 4, -2]
    >>> move_list([1, 2, -3, 3, -2, 0, 4], 7)
    [1, 2, -3, 4, 0, 3, -2]
    >>> move_list([811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612], 7)
    [-2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153, 0]
    >>> move_list([811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612], 70)
    [-2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153, 0]
    """
    positions = range(len(inp_list))
    new_positions = list(positions)
    for move in range(moves):
        move = move % len(inp_list)
        recent_pos = new_positions.index(move)
        new_positions.remove(move)
        shift = inp_list[move]
        new_pos = (recent_pos + shift) % (len(positions) - 1)
        if new_pos > 0:
            new_positions = new_positions[:new_pos] + [move] + new_positions[new_pos:]
        else:
            new_positions = new_positions + [move]
    return [inp_list[i] for i in new_positions]


def grove_coordinates_sum(moved_list: List[int]) -> int:
    """
    >>> grove_coordinates_sum([1, 2, -3, 4, 0, 3, -2])
    3
    >>> grove_coordinates_sum([0, -2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153])
    1623178306
    """
    zero_coord = moved_list.index(0)
    return sum(
        [
            moved_list[(zero_coord + j) % len(moved_list)]
            for j in [1000 * (1 + i) for i in range(3)]
        ]
    )


if __name__ == "__main__":
    with open("data/day20.txt", "r") as f:
        data = [int(x) for x in f.readlines()]

    moved_list = move_list(data, len(data))
    print(f"part1: {grove_coordinates_sum(moved_list)}")

    moved_list2 = move_list([d * 811589153 for d in data], 10 * len(data))
    print(f"part2: {grove_coordinates_sum(moved_list2)}")
