from dataclasses import dataclass
from collections import deque
from typing import List, Callable
import re
from math import prod


@dataclass
class Monkey:
    items: deque[int]
    operator: str
    operation_factor: str
    test_factor: int
    monkey_true: int
    monkey_false: int
    inspected_items: int = 0

    def operation(self, worry) -> int:
        factor = worry if self.operation_factor == "old" else int(self.operation_factor)
        if self.operator == "+":
            return worry + factor
        return worry * factor

    def test(self, worry) -> int:
        self.inspected_items += 1
        if (worry % self.test_factor) == 0:
            return self.monkey_true
        else:
            return self.monkey_false


EXAMPLE_INPUT = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def parse_monkeys(input_str: str) -> List[Monkey]:
    monkeys = []
    for monkey in input_str.split("\n\n"):
        operation_parsing = re.search(
            "Operation: new = old ([+*]) ([0-9]+|old)", monkey
        )
        monkeys.append(
            Monkey(
                items=deque(
                    [
                        int(item)
                        for item in re.search(r"Starting items: ([0-9, ]*)", monkey)
                        .group(1)
                        .split(",")
                    ]
                ),
                operator=operation_parsing.group(1),
                operation_factor=operation_parsing.group(2),
                test_factor=int(
                    re.search(r"Test: divisible by (\d+)", monkey).group(1)
                ),
                monkey_true=int(
                    re.search(r"If true: throw to monkey (\d)", monkey).group(1)
                ),
                monkey_false=int(
                    re.search(r"If false: throw to monkey (\d)", monkey).group(1)
                ),
            )
        )
    return monkeys


def let_monkeys_play(
    monkeys: List[Monkey], iterations: int, worry_manager: Callable[[int], int]
) -> List[Monkey]:
    for _ in range(iterations):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                worry = worry_manager(monkey.operation(item))
                next_monkey = monkey.test(worry)
                monkeys[next_monkey].items.append(worry)

    return monkeys


def calculate_monkey_business(monkeys: List[Monkey]) -> int:
    return prod(sorted([monkey.inspected_items for monkey in monkeys])[-2:])


if __name__ == "__main__":
    with open("data/day11.txt", "r") as f:
        data = f.read()

    print("part1")
    worry_manager_1 = lambda x: x // 3
    assert (
        calculate_monkey_business(
            let_monkeys_play(parse_monkeys(EXAMPLE_INPUT), 20, worry_manager_1)
        )
        == 10605
    )
    part1_solution = calculate_monkey_business(
        let_monkeys_play(parse_monkeys(data), 20, worry_manager_1)
    )
    print(part1_solution)
    assert part1_solution == 78678

    print("part2")
    monkeys = parse_monkeys(EXAMPLE_INPUT)
    worry_manager_2 = lambda x: x % prod([monkey.test_factor for monkey in monkeys])
    assert (
        calculate_monkey_business(let_monkeys_play(monkeys, 10_000, worry_manager_2))
        == 2713310158
    )
    monkeys = parse_monkeys(data)
    worry_manager_2 = lambda x: x % prod([monkey.test_factor for monkey in monkeys])
    part2_solution = calculate_monkey_business(
        let_monkeys_play(monkeys, 10_000, worry_manager_2)
    )
    print(part2_solution)
    assert part2_solution == 15333249714
