from math import atan2, pi


def distance_between_points(p1, p2):
    return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2


def angle_between_points(p1, p2):
    """
    >>> angle_between_points([0,0], [0, 2])
    3.141592653589793
    >>> angle_between_points([0,0], [2, 0])
    1.5707963267948966
    """
    return atan2(p2[0] - p1[0], p1[1] - p2[1]) % (2 * pi)


def get_all_angles_for_one_point(data, reference):
    """
    >>> get_all_angles_for_one_point([(0, 0), (0, 2), (2, 0)], (0, 0))
    {1.5707963267948966, 3.141592653589793}
    >>> get_all_angles_for_one_point([(0, 0), (0, 2), (2, 0), (4, 0)], (0, 0))
    {1.5707963267948966, 3.141592653589793}
    """
    return set([angle_between_points(reference, point) for point in data if point != reference])


def get_all_angles_dictionary(data, reference):
    """
    >>> get_all_angles_dictionary([(0, 0), (0, 2), (2, 0)], (0, 0))
    {1.5707963267948966: [(2, 0)], 3.141592653589793: [(0, 2)]}
    >>> get_all_angles_dictionary([(0, 0), (0, 2), (2, 0), (4, 0)], (0, 0))
    {1.5707963267948966: [(2, 0), (4, 0)], 3.141592653589793: [(0, 2)]}
    >>> get_all_angles_dictionary([(0, 0), (0, 2)], (0, 3))
    {0.0: [(0, 2), (0, 0)]}
    """
    return {angle: sorted([point for point in data
                           if angle_between_points(reference, point) == angle and point != reference],
                          key=lambda x: distance_between_points(x, reference), reverse=False)
            for angle in get_all_angles_for_one_point(data, reference)}


def get_asteroids(path):
    with open(path) as f:
        data = [(s, l) for l, line in enumerate(f.read().splitlines()) for s, string in enumerate(line) if string == "#"]
    return data


def part_1(path):
    """
    >>> part_1("./data/day10a.txt")
    ((5, 8), 33)
    >>> part_1("./data/day10b.txt")
    ((1, 2), 35)
    >>> part_1("./data/day10c.txt")
    ((6, 3), 41)
    >>> part_1("./data/day10d.txt")
    ((11, 13), 210)
    """
    data = get_asteroids(path)
    return sorted(map(lambda x: (x[0], len(x[1])),
                      list(map(lambda x: (x, get_all_angles_for_one_point(data, x)), data))),
                  key=lambda x: x[1], reverse=True)[0]


def part_2(path, reference, step):
    """
    >>> part_2("./data/day10e.txt", (8, 3), 6)
    (11, 1)
    >>> part_2("./data/day10d.txt", (11, 13), 2)
    (12, 1)
    >>> part_2("./data/day10d.txt", (11, 13), 200)
    (8, 2)
    """
    data = get_asteroids(path)
    angles_dict = get_all_angles_dictionary(data, reference)
    i = 1
    while True:
        for angle in sorted(angles_dict):
            asteroid = angles_dict.get(angle)
            if asteroid:
                vapored = angles_dict[angle].pop(0)
                if i == step:
                    return vapored
                i += 1


if __name__ == "__main__":
    print("PART ONE")
    print(part_1("./data/day10.txt"))

    print("PART TWO")
    print(part_2("./data/day10.txt", (28, 29), 200))
