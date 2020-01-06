import numpy as np
from collections import Counter


def convert_to_array(number_string):
    """
    >>> convert_to_array('123455')
    array([1, 2, 3, 4, 5, 5])
    """
    return np.array([int(i) for i in str(number_string)])


def has_number_of_digits(numbers, n=6):
    """
    >>> has_number_of_digits(np.array([1, 2, 3, 4, 5, 6]))
    True
    >>> has_number_of_digits(np.array([1, 2, 3, 4, 5]))
    False
    """
    return len(numbers) == n


def get_derivative(numbers):
    """
    >>> get_derivative(np.array([1, 2, 3, 1]))
    array([ 1,  1, -2])
    """
    return (np.roll(numbers, -1) - numbers)[:-1]


def two_adjacent_numbers_are_the_same(numbers):
    """
    >>> two_adjacent_numbers_are_the_same(np.array([1, 1, 4, 1, 0, 2]))
    True
    >>> two_adjacent_numbers_are_the_same(np.array([1, 1, 1, 1, 1, 1]))
    True
    >>> two_adjacent_numbers_are_the_same(np.array([1, 2, 4, 1, 0, 2]))
    False
    """
    return np.any(get_derivative(numbers) == 0)


def digits_never_decrease(numbers):
    """
    >>> digits_never_decrease(np.array([1, 2, 3, 4, 5, 6]))
    True
    >>> digits_never_decrease(np.array([1, 1, 3, 4, 5, 6]))
    True
    >>> digits_never_decrease(np.array([1, 2, 1, 4, 5, 6]))
    False
    """
    return np.all(get_derivative(numbers) >= 0)


def password_check(numbers):
    """
    >>> password_check('111111')
    True
    >>> password_check('223450')
    False
    >>> password_check('123789')
    False
    """
    numbers = convert_to_array(numbers)
    return (
            has_number_of_digits(numbers)
            and two_adjacent_numbers_are_the_same(numbers)
            and digits_never_decrease(numbers)
            )


def password_check_part2(numbers):
    """
    >>> password_check_part2('112233')
    True
    >>> password_check_part2('123444')
    False
    >>> password_check_part2('111122')
    True
    """
    numbers = convert_to_array(numbers)
    return (
            has_number_of_digits(numbers)
            and two_adjacent_numbers_are_the_same(numbers)
            and digits_never_decrease(numbers)
            and (2 in Counter(numbers).values())
            )


if __name__ == "__main__":
    PUZZLE_INPUT = "134564-585159"
    number_from, number_to = map(int, PUZZLE_INPUT.split("-"))
    input_range = np.arange(number_from, number_to+1)

    print('PART ONE')
    part_one = list(map(password_check, input_range)).count(True)
    print(part_one)
    assert part_one == 1929

    print('PART TWO')
    part_two = list(map(password_check_part2, input_range)).count(True)
    print(part_two)
    assert part_two == 1306
