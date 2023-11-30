def part1(raw_input):
    """
    >>> part1('''939
    ... 7,13,x,x,59,x,31,19''')
    295
    """
    time, raw_busses = raw_input.splitlines()
    waiting_time = get_first_bus(int(time), [int(b) for b in raw_busses.split(",") if b != "x"])
    return waiting_time[0] * waiting_time[1]

def part2(raw_input):
    """
    >>> part2("17,x,13,19")
    3417
    >>> part2("1789,37,47,1889")
    1202161486
    """
    departures = {i: int(bus) for i, bus in enumerate(raw_input.split(",")) if bus != "x"}
    time = 100000000000000
    while not depart_in_a_row(time, departures):
        time += departures[0]
    return time

def depart_in_a_row(time, departures):
    """
    >>> depart_in_a_row(0, {0: 17, 2: 13, 3: 19})
    False
    >>> depart_in_a_row(3417, {0: 17, 2: 13, 3: 19})
    True
    """
    return all((time + t) % bus == 0 for t, bus in departures.items())

def get_first_bus(time, busses):
    """
    >>> get_first_bus(939, [7, 13, 59, 31, 19])
    (59, 5)
    """
    waiting_times = {bus: get_waiting_time(time, bus) for bus in busses}
    return min(waiting_times.items(), key=lambda x: x[1])


def get_waiting_time(time, bus):
    """
    >>> get_waiting_time(939, 7)
    6
    >>> get_waiting_time(939, 59)
    5
    """
    departure = 0
    while departure < time:
        departure += bus
    return departure - time


if __name__ == "__main__":
    with open("data/day13.txt", "r") as f:
        data = f.read()
    
    print("PART 1")
    print(part1(data))

    print("PART 2")
    print(part2(data.splitlines()[1]))
