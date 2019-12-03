import numpy as np


def go_one_step(old_state, direction):
    """
    Takes old position and command and returns new position.
    >>> go_one_step((0,0), 'R')
    (1, 0)
    >>> go_one_step((1,1), 'L')
    (0, 1)
    >>> go_one_step((0,0), 'U')
    (0, 1)
    >>> go_one_step((-1,-1), 'D')
    (-1, -2)
    """
    assert direction in ['R', 'L', 'U', 'D']

    x, y = old_state
    if direction == 'R':
        return (x+1, y)
    if direction == 'L':
        return (x-1, y)
    if direction == 'U':
        return (x, y+1)
    if direction == 'D':
        return (x, y-1)


def apply_one_command(old_state, command):
    """
    Applies one command.
    >>> list(apply_one_command((1,1), 'R2'))
    [(2, 1), (3, 1)]
    """
    direction = command[0]
    times = int(command[1:])
    for i in range(times):
        old_state = go_one_step(old_state, direction)
        yield old_state


def get_one_path(commands):
    """
    Get one path, given a list of commands. Starting at (0, 0).
    >>> get_one_path(['R2', 'U1'])
    [(1, 0), (2, 0), (2, 1)]
    """
    path = []
    last_position = (0, 0)
    for command in commands:
        path += list(apply_one_command(last_position, command))
        last_position = path[-1]
    return path


def get_distance_of_closest_intersections(commands1, commands2):
    """
    Takes two paths and returns distance of closest intersection
    >>> get_distance_of_closest_intersections(
    ...   ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    ...   ['U62', 'R66' ,'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    ...   )
    159
    >>> get_distance_of_closest_intersections(
    ...   ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
    ...   ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    ...   )
    135
    """
    path1 = get_one_path(commands1)
    path2 = get_one_path(commands2)
    intersections = set(path1).intersection(set(path2))
    return min(map(lambda x: np.abs(x[0])+np.abs(x[1]), intersections))


def get_steps_of_closest_intersections(commands1, commands2):
    """
    Takes two paths and returns distance of closest intersection
    >>> get_steps_of_closest_intersections(
    ...   ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    ...   ['U62', 'R66' ,'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    ...   )
    610
    >>> get_steps_of_closest_intersections(
    ...   ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
    ...   ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    ...   )
    410
    """

    path1 = get_one_path(commands1)
    path2 = get_one_path(commands2)
    intersections = set(path1).intersection(set(path2))
    # index is 0 based, therefore +2
    return min(path1.index(intersection) + path2.index(intersection) for intersection in intersections) + 2


with open("./data/day03.txt") as f:
    data = f.readlines()

data = list(map(lambda x: x.split(','), data))

print("PART ONE")
print(get_distance_of_closest_intersections(data[0], data[1]))
assert get_distance_of_closest_intersections(data[0], data[1]) == 855

print("PART TWO")
print(get_steps_of_closest_intersections(data[0], data[1]))
assert get_steps_of_closest_intersections(data[0], data[1]) == 11238
