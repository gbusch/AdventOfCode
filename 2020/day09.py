from collections import deque

def part1(all_numbers, window_len):
    """
    >>> part1([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 5)
    127
    """
    for i, number in enumerate(all_numbers[window_len:]):
        if not is_sum_of_list(number, all_numbers[i:i + window_len]):
            return number
    return None


def part2(all_numbers, step1_number):
    """
    >>> part2([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 127)
    62
    """
    numbers = deque()
    for number in all_numbers:
        numbers.appendleft(number)
        while sum(numbers) > step1_number:
            numbers.pop()
        if sum(numbers) == step1_number:
            return min(numbers) + max(numbers)
        else:
            pass


def is_sum_of_list(number, numbers_list):
    """
    >>> is_sum_of_list(26, range(1, 26))
    True
    >>> is_sum_of_list(49, range(1, 26))
    True
    >>> is_sum_of_list(100, range(1, 26))
    False
    >>> is_sum_of_list(50, range(1, 26))
    False
    """
    for i, num1 in enumerate(numbers_list):
        for j, num2 in enumerate(numbers_list[i+1:]):
            if num1 + num2 == number:
                return True
    return False


if __name__ == "__main__":
    with open("./data/day09.txt", "r") as f:
        data = f.readlines()
    data = list(map(int, data))
    
    print("PART 1")
    result1 = part1(data, 25)
    print(result1)

    print("PART 2")
    print(part2(data, result1))