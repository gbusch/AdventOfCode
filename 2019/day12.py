from collections import namedtuple
MoonState = namedtuple('MoonState', 'position velocity')


def apply_velocity(moon: MoonState):
    """
    >>> apply_velocity(MoonState((1, 2, 3), (2, -1, 1)))
    MoonState(position=(3, 1, 4), velocity=(2, -1, 1))
    """
    return MoonState(position=tuple(p + v for p, v in zip(moon.position, moon.velocity)),
                     velocity=moon.velocity)


def apply_gravity(moon1: MoonState, moon2: MoonState):
    """
    >>> apply_gravity(MoonState((1, 2, 3), (2, -1, 1)), MoonState((3, 4, 1), (-2, -1, 2)))
    MoonState(position=(1, 2, 3), velocity=(3, 0, 0))
    >>> apply_gravity(MoonState((3, 4, 1), (-2, -1, 2)), MoonState((1, 2, 3), (2, -1, 1)))
    MoonState(position=(3, 4, 1), velocity=(-3, -2, 3))
    """
    return MoonState(position=moon1.position,
                     velocity=tuple(v+1 if p1 > p else (v-1 if p > p1 else v)
                                    for v, p, p1 in zip(moon1.velocity, moon1.position, moon2.position)))


def go_N_steps(moons, max_steps=1, steps=None):
    """
    >>> moon1 = MoonState(position=(-1, 0, 2), velocity=(0, 0, 0))
    >>> moon2 = MoonState(position=(2, -10, -7), velocity=(0, 0, 0))
    >>> moon3 = MoonState(position=(4, -8, 8), velocity=(0, 0, 0))
    >>> moon4 = MoonState(position=(3, 5, -1), velocity=(0, 0, 0))
    >>> result = go_N_steps([moon1, moon2, moon3, moon4])
    >>> list(result)[0][0]
    MoonState(position=(2, -1, 1), velocity=(3, -1, -1))
    >>> result = go_N_steps([moon1, moon2, moon3, moon4], max_steps=5)
    >>> list(result)[0][2]
    MoonState(position=(2, 2, -4), velocity=(0, -1, 2))
    >>> result = go_N_steps([moon1, moon2, moon3, moon4], max_steps=10)
    >>> list(result)[0][1]
    MoonState(position=(1, -8, 0), velocity=(-1, 1, 3))
    """
    if not steps:
        steps = 1
    one_step = go_step(moons)
    if steps < max_steps:
        return go_N_steps(one_step, max_steps, steps + 1)
    return one_step, max_steps, steps + 1


def steps_till_previous_point(start_positions, moon_no):
    """
    >>> steps_till_previous_point(((-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)), 0)
    924
    >>> steps_till_previous_point(((-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)), 1)
    2772
    """
    start_moons = tuple(MoonState(position=pos, velocity=(0,)) for pos in start_positions)
    moons = start_moons
    steps = 0
    while True:
        moons = go_step(moons)
        steps += 1
        if moons[moon_no] == start_moons[moon_no]:
            return steps


def go_step(moons):
    from functools import reduce
    gravity_applied = [reduce(apply_gravity, moons[i:] + moons[:i]) for i in range(len(moons))]
    velocity_applied = tuple(map(apply_velocity, gravity_applied))
    return velocity_applied


def moon_energy(moon: MoonState):
    """
    >>> moon_energy(MoonState(position=(2, 1, -3), velocity=(-3, -2, 1)))
    36
    """
    return sum(map(abs, moon.position)) * sum(map(abs, moon.velocity))


def total_energy(moons):
    """
    >>> moon1 = MoonState(position=(2, 1, -3), velocity=(-3, -2, 1))
    >>> moon2 = MoonState(position=(1, -8, 0), velocity=(-1, 1, 3))
    >>> moon3 = MoonState(position=(3, -6, 1), velocity=(3, 2, -3))
    >>> moon4 = MoonState(position=(2, 0, 4), velocity=(1, -1, -1))
    >>> total_energy([moon1, moon2, moon3, moon4])
    179
    """
    return sum(map(moon_energy, moons))


def total_energy_after_N_steps(start_positions, steps):
    """
    >>> total_energy_after_N_steps([(-8, -10, 0), (5, 5, 10), (2, -7, 3), (9, -8, -3)], 100)
    1940
    """
    moons = tuple(MoonState(position=pos, velocity=(0, 0, 0)) for pos in start_positions)
    state_after_steps = go_N_steps(moons, max_steps=steps)[0]
    return total_energy(state_after_steps)


def lcm(a, b):
    from math import gcd
    return abs(a*b) // gcd(a, b)


if __name__ == "__main__":
    #start_positions = ((14, 2, 8), (7, 4, 10), (1, 17, 16), (-4, -1, 1))

    #print("PART ONE")
    #import sys; sys.setrecursionlimit(10000)
    #total_energy_1000_steps = total_energy_after_N_steps(start_positions, 1000)
    #print(total_energy_1000_steps)
    #assert total_energy_1000_steps == 9139

    print("PART TWO")
    start_positions = ((-8,), (5,), (2,), (9,))
    steps_x = steps_till_previous_point(start_positions, 0)
    start_positions = ((-10,), (5,), (-7,), (-8,))
    steps_y = steps_till_previous_point(start_positions, 0)
    start_positions = ((0,), (10,), (3,), (-3,))
    steps_z = steps_till_previous_point(start_positions, 0)
    print(steps_x, steps_y, steps_z)

    ### 2028 60 57

    #start_positions = ((14,), (7,), (1,), (-4,))
    #steps_x = steps_till_previous_point(start_positions, 0)
    #start_positions = ((2,), (4,), (17,), (-1,))
    #steps_y = steps_till_previous_point(start_positions, 0)
    #start_positions = ((8,), (10,), (16,), (1,))
    #steps_z = steps_till_previous_point(start_positions, 0)
    #print(steps_x, steps_y, steps_z)
    #print(lcm(steps_x, lcm(steps_y, steps_z)))
