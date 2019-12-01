def fuel_per_module(mass):
    """
    Returns fuel required for each module.
    To find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
    >>> fuel_per_module(12)
    2
    >>> fuel_per_module(14)
    2
    >>> fuel_per_module(1969)
    654
    >>> fuel_per_module(100756)
    33583
    """
    return (mass // 3) - 2


def all_fuel_per_module(mass):
    """
    Returns all fuel, including the fuel for the fuel.
    >>> all_fuel_per_module(14)
    2
    >>> all_fuel_per_module(1969)
    966
    >>> all_fuel_per_module(100756)
    50346
    """
    additional_fuel = fuel_per_module(mass)
    if additional_fuel < 0:
        return 0
    else:
        return additional_fuel + all_fuel_per_module(additional_fuel)


with open("./data/day01.txt") as f:
    data = f.read().splitlines()

data = list(map(int, data))

print("PART ONE")
total_fuel = sum(map(fuel_per_module, data))
print(total_fuel)


print("PART TWO")
total_fuel = sum(map(all_fuel_per_module, data))
print(total_fuel)

