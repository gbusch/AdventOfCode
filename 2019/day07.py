def intcode_calculation(integers, input_values=[1], position=0):
    """
    Intcode program.
    >>> intcode_calculation([1, 0, 0, 0, 99])[0]
    [2, 0, 0, 0, 99]
    >>> intcode_calculation([2, 3, 0, 3, 99])[0]
    [2, 3, 0, 6, 99]
    >>> intcode_calculation([2, 4, 4, 5, 99, 0])[0]
    [2, 4, 4, 5, 99, 9801]
    >>> intcode_calculation([1, 1, 1, 4, 99, 5, 6, 0, 99])[0]
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    >>> intcode_calculation([3, 0, 4, 0, 99])[0]
    [1, 0, 4, 0, 99]
    >>> intcode_calculation([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input_values=[0])[1]
    0
    >>> intcode_calculation([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input_values=[1])[1]
    1
    >>> intcode_calculation([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input_values=[0])[1]
    0
    >>> intcode_calculation([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input_values=[1])[1]
    1
    """

    opcode = opcode_decoder(integers[position])

    while opcode.opcode != 99:
        def get_value(param):
            if opcode.modes[param-1] == 0:
                return integers[integers[position + param]]
            if opcode.modes[param-1] == 1:
                return integers[position + param]

        if opcode.opcode == 1:
            integers[integers[position + 3]] = get_value(1) + get_value(2)
            position += 4
        elif opcode.opcode == 2:
            integers[integers[position + 3]] = get_value(1) * get_value(2)
            position += 4
        elif opcode.opcode == 3:
            integers[integers[position + 1]] = input_values.pop()
            position += 2
        elif opcode.opcode == 4:
            output = get_value(1)
            position += 2
            return integers, output, position, True
        elif opcode.opcode == 5:
            if get_value(1) != 0:
                position = get_value(2)
            else:
                position += 3
        elif opcode.opcode == 6:
            if get_value(1) == 0:
                position = get_value(2)
            else:
                position += 3
        elif opcode.opcode == 7:
            if get_value(1) < get_value(2):
                integers[integers[position + 3]] = 1
            else:
                integers[integers[position + 3]] = 0
            position += 4
        elif opcode.opcode == 8:
            if get_value(1) == get_value(2):
                integers[integers[position + 3]] = 1
            else:
                integers[integers[position + 3]] = 0
            position += 4
        else:
            raise Exception(f"got opcode {opcode.opcode}")

        opcode = opcode_decoder(integers[position])

    return integers, input_values[0], position, False


def opcode_decoder(opcode):
    """
    >>> opcode_decoder(1002)
    Opcode(opcode=2, modes=[0, 1, 0])
    >>> opcode_decoder(101)
    Opcode(opcode=1, modes=[1, 0, 0])
    """
    from collections import namedtuple
    Opcode = namedtuple('Opcode', 'opcode modes')

    opcode_full = f'{opcode:05d}'

    return Opcode(opcode=int(opcode_full[3:]),
                  modes=[int(opcode_full[2]), int(opcode_full[1]), int(opcode_full[0])])


def run_amplifiers(integers, setting_sequence):
    """
    >>> run_amplifiers([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], [4, 3, 2, 1, 0])
    43210
    >>> run_amplifiers([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0,1,2,3,4])
    54321
    >>> run_amplifiers([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2])
    65210
    """
    assert sorted(setting_sequence) == [0, 1, 2, 3, 4]
    output = 0
    for phase in setting_sequence:
        _, output, _, _ = intcode_calculation(integers.copy(), [output, phase])
    return output


def run_amplifiers_with_feedback(integers, setting_sequence):
    """
    >>> run_amplifiers_with_feedback([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [9,8,7,6,5])
    139629729
    >>> run_amplifiers_with_feedback([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10], [9,7,8,5,6])
    18216
    """
    integer_memory = dict()
    output = 0
    position_memory = dict()

    for i, phase in enumerate(setting_sequence):
        integer_memory[i], output, position_memory[i], running = intcode_calculation(integers.copy(), [output, phase])
    i = 0
    while running:
        integer_memory[i], output, position_memory[i], running = intcode_calculation(integer_memory[i], [output], position_memory[i])
        i = (i+1) % 5
    return output


def part_1(integers):
    from itertools import permutations
    sequences = permutations(range(5))
    return max(map(lambda x: run_amplifiers(integers.copy(), x), sequences))


def part_2(integers):
    from itertools import permutations
    sequences = permutations(range(5, 10))
    return max(map(lambda x: run_amplifiers_with_feedback(integers.copy(), x), sequences))


with open("./data/day07.txt") as f:
    data = list(map(int, f.readline().split(",")))


print("PART ONE")
print(part_1(data))

print("PART TWO")
print(part_2(data))
