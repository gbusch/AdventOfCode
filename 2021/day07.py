import sys
import numpy as np
from functools import cache
from typing import Callable

sys.setrecursionlimit(10000)


def minimize_fuel(initial: list[int], metric: Callable[[list[int], int], int]) -> int:
    """
    >>> minimize_fuel([16,1,2,0,4,2,7,1,2,14], fuel_consumption)
    37
    >>> minimize_fuel([16,1,2,0,4,2,7,1,2,14], crab_fuel_consumption)
    168
    """
    possible_ends = np.arange(min(initial), max(initial))
    return min(np.vectorize(lambda x: metric(initial, x))(possible_ends))


def fuel_consumption(initial: list[int], final: int) -> int:
    """
    >>> fuel_consumption([16,1,2,0,4,2,7,1,2,14], 2)
    37
    >>> fuel_consumption([16,1,2,0,4,2,7,1,2,14], 10)
    71
    """
    return int(np.linalg.norm(np.array(initial) - final, 1))


def crab_fuel_consumption(initial: list[int], final: int) -> int:
    """
    >>> crab_fuel_consumption([16,1,2,0,4,2,7,1,2,14], 2)
    206
    >>> crab_fuel_consumption([16,1,2,0,4,2,7,1,2,14], 5)
    168
    """
    return int(sum(map(crab_distance, np.abs(np.array(initial) - final))))


@cache
def crab_distance(n: int) -> int:
    """
    >>> crab_distance(1)
    1
    >>> crab_distance(2)
    3
    >>> crab_distance(11)
    66
    """
    return n + crab_distance(n - 1) if n > 0 else 0


if __name__ == "__main__":
    with open("data/day07.txt", "r") as f:
        inlist = [int(x) for x in f.read().split(",")]

    print(f"Part 1: {minimize_fuel(inlist, fuel_consumption)}")
    print(f"Part 2: {minimize_fuel(inlist, crab_fuel_consumption)}")
