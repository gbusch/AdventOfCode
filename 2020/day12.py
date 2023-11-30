from collections import namedtuple, deque
from functools import reduce

State = namedtuple("State", "x y direction")
Command = namedtuple("Command", "command number")


def part1(raw_input):
    """
    >>> part1('''F10
    ... N3
    ... F7
    ... R90
    ... F11''')
    25
    >>> part1('''E2
    ... L180
    ... S4
    ... R90
    ... S1
    ... F49''')
    46
    """
    commands = [parse_command(raw_command) for raw_command in raw_input.splitlines()]
    last_pos = reduce(lambda state, command: move(state, command), commands, State(x=0, y=0, direction='E'))
    return abs(last_pos.x) + abs(last_pos.y)

def move(state, command):
    """
    >>> move(State(x=0, y=0, direction='E'), Command(command='F', number=10))
    State(x=10, y=0, direction='E')
    >>> move(State(x=10, y=0, direction='E'), Command(command='N', number=3))
    State(x=10, y=3, direction='E')
    >>> move(State(x=10, y=0, direction='E'), Command(command='W', number=3))
    State(x=7, y=0, direction='E')
    >>> move(State(x=10, y=0, direction='E'), Command(command='E', number=3))
    State(x=13, y=0, direction='E')
    >>> move(State(x=10, y=3, direction='E'), Command(command='F', number=7))
    State(x=17, y=3, direction='E')
    >>> move(State(x=17, y=3, direction='E'), Command(command='R', number=90))
    State(x=17, y=3, direction='S')
    >>> move(State(x=17, y=3, direction='E'), Command(command='L', number=90))
    State(x=17, y=3, direction='N')
    >>> move(State(x=17, y=3, direction='E'), Command(command='R', number=270))
    State(x=17, y=3, direction='N')
    >>> move(State(x=17, y=3, direction='S'), Command(command='F', number=11))
    State(x=17, y=-8, direction='S')
    """

    if command.command in ["R", "L"]:
        rotation = deque(["N", "E", "S", "W"])
        dir = {"R": 1, "L": -1}[command.command]
        rotation.rotate(-(rotation.index(state.direction) + dir * command.number//90))
        return State(x=state.x, y=state.y, direction=rotation[0])

    action = state.direction if command.command == "F" else command.command
    x = {"E": state.x + command.number, "W": state.x - command.number}.get(action, state.x)
    y = {"N": state.y + command.number, "S": state.y - command.number}.get(action, state.y)
    return State(x=x, y=y, direction=state.direction)

def parse_command(raw_command):
    """
    >>> parse_command("R90")
    Command(command='R', number=90)
    >>> parse_command("F11")
    Command(command='F', number=11)
    """
    return Command(command=raw_command[0], number=int(raw_command[1:]))


if __name__ == "__main__":
    with open("data/day12.txt", "r") as f:
        data = f.read()
    
    print("PART 1")
    print(part1(data))