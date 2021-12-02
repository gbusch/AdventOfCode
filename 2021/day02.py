from dataclasses import dataclass

@dataclass
class Position:
    horizontal: int
    vertical: int
    aim: int = 0

    def multiply(self) -> int:
        """
        >>> pos = Position(2, 3)
        >>> pos.multiply()
        6
        """
        return self.horizontal * self.vertical
    
    def move(self, instruction: str) -> None:
        """
        >>> pos = Position(0, 0)
        >>> pos.move("forward 5")
        >>> pos
        Position(horizontal=5, vertical=0, aim=0)
        >>> pos.move("down 5")
        >>> pos
        Position(horizontal=5, vertical=5, aim=0)
        >>> pos.move("forward 8")
        >>> pos
        Position(horizontal=13, vertical=5, aim=0)
        >>> pos.move("up 3")
        >>> pos
        Position(horizontal=13, vertical=2, aim=0)
        """
        direction, count = instruction.split()
        assert direction in ["forward", "up", "down"]
        if direction == "forward":
            self.horizontal += int(count)
        if direction == "up":
            self.vertical -= int(count)
        if direction == "down":
            self.vertical += int(count)
    
    def move_with_aim(self, instruction: str) -> None:
        """
        >>> pos = Position(0, 0)
        >>> pos.move_with_aim("forward 5")
        >>> pos
        Position(horizontal=5, vertical=0, aim=0)
        >>> pos.move_with_aim("down 5")
        >>> pos.move_with_aim("forward 8")
        >>> pos
        Position(horizontal=13, vertical=40, aim=5)
        >>> pos.move_with_aim("up 3")
        >>> pos.move_with_aim("down 8")
        >>> pos.move_with_aim("forward 2")
        >>> pos
        Position(horizontal=15, vertical=60, aim=10)
        """
        direction, count = instruction.split()
        assert direction in ["forward", "up", "down"]
        if direction == "forward":
            self.horizontal += int(count)
            self.vertical += int(count) * self.aim
        if direction == "up":
            self.aim -= int(count)
        if direction == "down":
            self.aim += int(count)


def part1(inp: str) -> int:
    """
    >>> inp = '''forward 5
    ... down 5
    ... forward 8
    ... up 3
    ... down 8
    ... forward 2'''
    >>> part1(inp)
    150
    """
    pos = Position(horizontal=0, vertical=0)
    for step in inp.splitlines():
        pos.move(step)
    return pos.multiply()


def part2(inp: str) -> int:
    """
    >>> inp = '''forward 5
    ... down 5
    ... forward 8
    ... up 3
    ... down 8
    ... forward 2'''
    >>> part2(inp)
    900
    """
    pos = Position(horizontal=0, vertical=0)
    for step in inp.splitlines():
        pos.move_with_aim(step)
    return pos.multiply()


if __name__ == "__main__":
    with open("data/day02.txt", "r") as f:
        inp = f.read()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
