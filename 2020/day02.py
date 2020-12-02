from collections import namedtuple, Counter

Rule = namedtuple("Rule", "letter num1 num2")


def part1(inlist):
    """
    >>> part1(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
    2
    """
    return sum(map(lambda x: password_valid1(*parse_line(x)), inlist))

def part2(inlist):
    """
    >>> part2(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
    1
    """
    return sum(map(lambda x: password_valid2(*parse_line(x)), inlist))

def password_valid1(password, rule):
    """
    >>> password_valid1("abcde", Rule(letter='a', num1=1, num2=3))
    True
    >>> password_valid1("cdefg", Rule(letter='b', num1=1, num2=3))
    False
    >>> password_valid1("ccccccccc", Rule(letter='c', num1=2, num2=9))
    True
    """
    if rule.num1 <= Counter(password).get(rule.letter, 0) <= rule.num2:
        return True
    return False

def password_valid2(password, rule):
    """
    >>> password_valid2("abcde", Rule(letter='a', num1=1, num2=3))
    True
    >>> password_valid1("cdefg", Rule(letter='b', num1=1, num2=3))
    False
    >>> password_valid2("ccccccccc", Rule(letter='c', num1=2, num2=9))
    False
    """
    return (password[rule.num1 - 1] == rule.letter) ^ (password[rule.num2 - 1] == rule.letter)

def parse_line(line):
    """
    >>> parse_line("1-3 a: abcde")
    ('abcde', Rule(letter='a', num1=1, num2=3))
    >>> parse_line("1-3 b: cdefg")
    ('cdefg', Rule(letter='b', num1=1, num2=3))
    >>> parse_line("2-9 c: ccccccccc")
    ('ccccccccc', Rule(letter='c', num1=2, num2=9))
    """
    raw_rule, password = line.split(":")
    raw_occ, raw_letter = raw_rule.split()
    return password.strip(), Rule(letter=raw_letter, num1=int(raw_occ.split("-")[0]), num2=int(raw_occ.split("-")[1]))


if __name__ == "__main__":
    with open("data/day02.txt", "r") as f:
        inlist = f.read().splitlines()

    print("PART 1")
    print(part1(inlist))

    print("PART 2")
    print(part2(inlist))