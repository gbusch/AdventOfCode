import numpy as np
from collections import namedtuple


Visit = namedtuple('Visit', 'position steps')


def go_one_step(old_state, direction):
    """
    Takes old position and command and returns new position.
    >>> go_one_step(Visit(position=(0,0), steps=0), 'R')
    Visit(position=(1, 0), steps=1)
    >>> go_one_step(Visit(position=(1,1), steps=1), 'L')
    Visit(position=(0, 1), steps=2)
    >>> go_one_step(Visit(position=(0,0), steps=2), 'U')
    Visit(position=(0, 1), steps=3)
    >>> go_one_step(Visit(position=(-1,-1), steps=3), 'D')
    Visit(position=(-1, -2), steps=4)
    """
    assert direction in ['R', 'L', 'U', 'D']

    x, y = old_state.position
    s = old_state.steps
    if direction == 'R':
        return Visit(position=(x+1, y), steps=s+1)
    if direction == 'L':
        return Visit(position=(x-1, y), steps=s+1)
    if direction == 'U':
        return Visit(position=(x, y+1), steps=s+1)
    if direction == 'D':
        return Visit(position=(x, y-1), steps=s+1)


def apply_one_command(old_state, command):
    """
    Applies one command.
    >>> list(apply_one_command(Visit(position=(1,1), steps=2), 'R2'))
    [Visit(position=(2, 1), steps=3), Visit(position=(3, 1), steps=4)]
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
    [Visit(position=(1, 0), steps=1), Visit(position=(2, 0), steps=2), Visit(position=(2, 1), steps=3)]
    """
    path = []
    last_position = Visit(position=(0, 0), steps=0)
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
    path1 = (visit.position for visit in get_one_path(commands1))
    path2 = (visit.position for visit in get_one_path(commands2))
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

    def convert_to_dict(visit):
        visit_dict = dict()
        for v in visit:
            if v.position not in visit_dict:
                visit_dict[v.position] = v.steps
            if (v.position in visit_dict) and (v.steps < visit_dict[v.position]):
                visit_dict[v.position] = v.steps
        return visit_dict

    path1 = convert_to_dict(get_one_path(commands1))
    path2 = convert_to_dict(get_one_path(commands2))

    intersections = set(path1.keys()).intersection(path2.keys())
    distances = [path1[i]+path2[i] for i in intersections]

    return min(distances)


with open("./data/day03.txt") as f:
    data = f.readlines()

data = list(map(lambda x: x.split(','), data))

print("PART ONE")
print(get_distance_of_closest_intersections(data[0], data[1]))
assert get_distance_of_closest_intersections(data[0], data[1]) == 855

print("PART TWO")
print(get_steps_of_closest_intersections(data[0], data[1]))
assert get_steps_of_closest_intersections(data[0], data[1]) == 11238
