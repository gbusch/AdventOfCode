import re
from typing import Dict

def part1(raw_input: str) -> int:
    """
    >>> part1('''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    ... byr:1937 iyr:2017 cid:147 hgt:183cm
    ...
    ... iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    ... hcl:#cfa07d byr:1929
    ...
    ... hcl:#ae17e1 iyr:2013
    ... eyr:2024
    ... ecl:brn pid:760753108 byr:1931
    ... hgt:179cm
    ...
    ... hcl:#cfa07d eyr:2025 pid:166559648
    ... iyr:2011 ecl:brn hgt:59in''')
    2
    """
    return sum(check_keys(parse_passport(line)) for line in raw_input.split("\n\n"))

def part2(raw_input: str) -> int:
    """
    >>> part2('''eyr:1972 cid:100
    ... hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
    ...
    ... iyr:2019
    ... hcl:#602927 eyr:1967 hgt:170cm
    ... ecl:grn pid:012533040 byr:1946
    ...
    ... hcl:dab227 iyr:2012
    ... ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
    ...
    ... hgt:59cm ecl:zzz
    ... eyr:2038 hcl:74454a iyr:2023
    ... pid:3556412378 byr:2007
    ...
    ... pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    ... hcl:#623a2f
    ...
    ... eyr:2029 ecl:blu cid:129 byr:1989
    ... iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
    ...
    ... hcl:#888785
    ... hgt:164cm byr:2001 iyr:2015 cid:88
    ... pid:545766238 ecl:hzl
    ... eyr:2022
    ...
    ... iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719''')
    4
    """
    return sum(validate_passport(parse_passport(line)) for line in raw_input.split("\n\n"))


def parse_passport(raw_line: str) -> Dict[str, str]:
    """
    >>> parse_passport("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm")
    {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
    >>> parse_passport("iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929")
    {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'}
    """
    return {k.split(":")[0]: k.split(":")[1] for k in raw_line.split()}

def validate_passport(passport: Dict[str, str]) -> bool:
    """
    >>> validate_passport({'pid': '087499704', 'hgt': '74in', 'ecl': 'grn', 'iyr': '2012', 'eyr': '2030', 'byr': '1980', 'hcl': '#623a2f'})
    True
    >>> validate_passport({'eyr': '1972', 'cid': '100', 'hcl': '#18171d', 'ecl': 'amb', 'hgt': '170', 'pid': '186cm', 'iyr': '2018', 'byr': '1926'})
    False
    """
    if not check_keys(passport): return False
    return all([
        check_birthyear(passport['byr']),
        check_issueyear(passport['iyr']),
        check_expiration(passport['eyr']),
        check_height(passport['hgt']),
        check_hair(passport['hcl']),
        check_eye(passport['ecl']),
        check_pid(passport['pid']),
    ])

def check_keys(passport: Dict[str, str]) -> bool:
    """
    >>> check_keys({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'})
    True
    >>> check_keys({'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'})
    False
    """
    mandatory_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(key in passport for key in mandatory_keys)

def check_birthyear(byr: str) -> bool:
    """
    >>> check_birthyear("2002")
    True
    >>> check_birthyear("2003")
    False
    """
    return 1920 <= int(byr) <= 2002

def check_issueyear(iyr: str) -> bool:
    """
    >>> check_issueyear("2015")
    True
    >>> check_issueyear("2002")
    False
    """
    return 2010 <= int(iyr) <= 2020

def check_expiration(eyr: str) -> bool:
    """
    >>> check_expiration("2021")
    True
    >>> check_expiration("2002")
    False
    """
    return 2020 <= int(eyr) <= 2030

def check_height(height: str) -> bool:
    """
    >>> check_height("60in")
    True
    >>> check_height("190cm")
    True
    >>> check_height("190in")
    False
    >>> check_height("190")
    False
    """
    if height[-2:] == "in":
        return 59 <= int(height[:-2]) <= 76
    if height[-2:] == "cm":
        return 150 <= int(height[:-2]) <= 193
    return False

def check_hair(hcl: str) -> bool:
    """
    >>> check_hair("#123abc")
    True
    >>> check_hair("#123abz")
    False
    >>> check_hair("123abc")
    False
    """
    return bool(re.match(r"^#[0-9a-f]{6}$", hcl))

def check_eye(ecl: str) -> bool:
    """
    >>> check_eye("brn")
    True
    >>> check_eye("wat")
    False
    """
    return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def check_pid(pid: str) -> bool:
    """
    >>> check_pid("000000001")
    True
    >>> check_pid("0123456789")
    False
    """
    return bool(re.match(r"^[0-9]{9}$", pid))



if __name__ == "__main__":
    with open("./data/day04.txt", "r") as f:
        raw_input = f.read()
    
    print("PART 1")
    print(part1(raw_input))

    print("PART 2")
    print(part2(raw_input))
