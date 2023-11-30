import re
from functools import reduce
from typing import Dict, Set

def part1(raw_input: str) -> int:
    """
    >>> part1('''light red bags contain 1 bright white bag, 2 muted yellow bags.
    ... dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    ... bright white bags contain 1 shiny gold bag.
    ... muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    ... shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    ... dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    ... vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    ... faded blue bags contain no other bags.
    ... dotted black bags contain no other bags.''')
    4
    """
    rules = reduce(lambda x, y: x.update(parse_rule(y)) or x, raw_input.splitlines(), {})
    return sum([contains_shiny_gold(rules, key) for key in rules.keys()])

def parse_rule(raw_rule: str) -> Dict[str, Set[str]]:
    """
    >>> parse_rule("light red bags contain 1 bright white bag, 2 muted yellow bags.") == {'light red': {'bright white', 'muted yellow'}}
    True
    >>> parse_rule("bright white bags contain 1 shiny gold bag.")
    {'bright white': {'shiny gold'}}
    >>> parse_rule("dotted black bags contain no other bags.")
    {'dotted black': set()}
    """
    bag, raw_content = raw_rule.split("bags contain")
    if raw_content.strip().startswith("no other"):
        content = set()
    else:
        content = set(re.search(r"\d (\w+ \w+) bag[s]?.?", bag.strip()).group(1) for bag in raw_content.split(","))
    return {bag.strip(): content}

def contains_shiny_gold(rules: Dict[str, Set[str]], bag: str) -> bool:
    """
    >>> contains_shiny_gold({'bright white': {'shiny gold'}}, 'bright white')
    True
    >>> contains_shiny_gold({'bright white': {'shiny gold'}, 'dark orange': {'bright white'}}, 'dark orange')
    True
    >>> contains_shiny_gold({'vibrant plum': {'faded blue', 'dotted black'}, 'faded blue': {}, 'dotted black': {}}, 'vibrant plum')
    False
    """
    if not rules[bag]:
        return False
    if 'shiny gold' in rules[bag]:
        return True
    return any([contains_shiny_gold(rules, content) for content in rules[bag]])


if __name__ == "__main__":
    with open("./data/day07.txt", "r") as f:
        data = f.read()
    
    print("PART 1")
    print(part1(data))
