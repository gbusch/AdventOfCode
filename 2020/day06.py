from functools import reduce


def part1(raw_input):
    """
    >>> part1('''abc
    ... 
    ... a
    ... b
    ... c
    ...
    ... ab
    ... ac
    ...
    ... a
    ... a
    ... a
    ... a
    ... 
    ... b''')
    11
    """
    return sum([unique_answers(group) for group in raw_input.split("\n\n")])

def part2(raw_input):
    """
    >>> part2('''abc
    ... 
    ... a
    ... b
    ... c
    ...
    ... ab
    ... ac
    ...
    ... a
    ... a
    ... a
    ... a
    ... 
    ... b''')
    6
    """
    return sum([mutual_answers(group) for group in raw_input.split("\n\n")])

def unique_answers(raw_group):
    """
    >>> unique_answers('''abc''')
    3
    >>> unique_answers('''a
    ... b
    ... c''')
    3
    >>> unique_answers('''ab
    ... ac''')
    3
    >>> unique_answers('''a
    ... a
    ... a
    ... a''')
    1
    """
    return len(set(a for aa in raw_group.splitlines() for a in aa))

def mutual_answers(raw_group):
    """
    >>> mutual_answers('''abc''')
    3
    >>> mutual_answers('''a
    ... b
    ... c''')
    0
    >>> mutual_answers('''ab
    ... ac''')
    1
    >>> mutual_answers('''a
    ... a
    ... a
    ... a''')
    1
    """
    return len(reduce(lambda x, y: x.intersection(y), [set(a) for a in raw_group.splitlines()]))

if __name__ == "__main__":
    with open("./data/day06.txt", "r") as f:
        data = f.read()
    
    print("PART 1")
    print(part1(data))

    print("PART 2")
    print(part2(data))
