def intcode_calculation(integers, input_values=[1]):
    """
    Intcode program.
    >>> intcode_calculation([1, 0, 0, 0, 99])[0]
    {0: 2, 1: 0, 2: 0, 3: 0, 4: 99}
    >>> intcode_calculation([2, 3, 0, 3, 99])[0]
    {0: 2, 1: 3, 2: 0, 3: 6, 4: 99}
    >>> intcode_calculation([2, 4, 4, 5, 99, 0])[0]
    {0: 2, 1: 4, 2: 4, 3: 5, 4: 99, 5: 9801}
    >>> intcode_calculation([1, 1, 1, 4, 99, 5, 6, 0, 99])[0]
    {0: 30, 1: 1, 2: 1, 3: 4, 4: 2, 5: 5, 6: 6, 7: 0, 8: 99}
    >>> intcode_calculation([3, 0, 4, 0, 99])[0]
    {0: 1, 1: 0, 2: 4, 3: 0, 4: 99}
    >>> intcode_calculation([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input_values=[0])[1][0]
    0
    >>> intcode_calculation([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input_values=[1])[1][0]
    1
    >>> intcode_calculation([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input_values=[0])[1][0]
    0
    >>> intcode_calculation([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input_values=[1])[1][0]
    1
    >>> intcode_calculation([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])[1]
    [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    >>> len(str(intcode_calculation([1102,34915192,34915192,7,4,7,99,0])[1][0]))
    16
    >>> intcode_calculation([104,1125899906842624,99])[1]
    [1125899906842624]
    """
    if isinstance(integers, list):
        integers = convert_to_dict(integers)

    position = 0
    opcode = opcode_decoder(integers.get(position, 0))
    output = []
    relative_base = 0

    while opcode.opcode != 99:
        def get_value(param):
            if opcode.modes[param-1] == 0:
                return integers.get(integers.get(position + param, 0), 0)
            elif opcode.modes[param-1] == 1:
                return integers.get(position + param, 0)
            elif opcode.modes[param-1] == 2:
                return integers.get(relative_base + integers.get(position + param, 0))
            else:
                raise Exception

        def write_position(parameter):
            if opcode.modes[parameter-1] == 0:
                return integers.get(position + parameter, 0)
            elif opcode.modes[parameter-1] == 2:
                return relative_base + integers.get(position + parameter, 0)
            else:
                raise Exception

        if opcode.opcode == 1:
            integers[write_position(3)] = get_value(1) + get_value(2)
            position += 4
        elif opcode.opcode == 2:
            integers[write_position(3)] = get_value(1) * get_value(2)
            position += 4
        elif opcode.opcode == 3:
            integers[write_position(1)] = input_values.pop()
            position += 2
        elif opcode.opcode == 4:
            output.append(get_value(1))
            position += 2
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
                integers[write_position(3)] = 1
            else:
                integers[write_position(3)] = 0
            position += 4
        elif opcode.opcode == 8:
            if get_value(1) == get_value(2):
                integers[write_position(3)] = 1
            else:
                integers[write_position(3)] = 0
            position += 4
        elif opcode.opcode == 9:
            relative_base += get_value(1)
            position += 2
        else:
            raise Exception

        opcode = opcode_decoder(integers.get(position, 0))

    return integers, output


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


def convert_to_dict(integer_list):
    """
    >>> convert_to_dict([1, 2, 3])
    {0: 1, 1: 2, 2: 3}
    """
    return {k: v for k, v in enumerate(integer_list)}


with open("./data/day09.txt") as f:
    data = list(map(int, f.read().split(',')))

print("PART ONE")
print(intcode_calculation(data, input_values=[1])[1])

print("PART TWO")
print(intcode_calculation(data, input_values=[2])[1])
