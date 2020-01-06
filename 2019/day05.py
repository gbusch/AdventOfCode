def intcode_calculation(integers, input_id=1):
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
    >>> intcode_calculation([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input_id=0)[1]
    0
    >>> intcode_calculation([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input_id=1)[1]
    1
    >>> intcode_calculation([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input_id=0)[1]
    0
    >>> intcode_calculation([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input_id=1)[1]
    1
    """

    position = 0
    opcode = opcode_decoder(integers[position])
    output = None

    while opcode.opcode != 99:
        def get_value(opcode, integers, param, position):
            if opcode.modes[param-1] == 0:
                return integers[integers[position + param]]
            if opcode.modes[param-1] == 1:
                return integers[position + param]

        if opcode.opcode == 1:
            integers[integers[position + 3]] = get_value(opcode, integers, 1, position) + get_value(opcode, integers, 2, position)
            position += 4
        elif opcode.opcode == 2:
            integers[integers[position + 3]] = get_value(opcode, integers, 1, position) * get_value(opcode, integers, 2, position)
            position += 4
        elif opcode.opcode == 3:
            integers[integers[position + 1]] = input_id
            position += 2
        elif opcode.opcode == 4:
            output = get_value(opcode, integers, 1, position)
            position += 2
        elif opcode.opcode == 5:
            if get_value(opcode, integers, 1, position) != 0:
                position = get_value(opcode, integers, 2, position)
            else:
                position += 3
        elif opcode.opcode == 6:
            if get_value(opcode, integers, 1, position) == 0:
                position = get_value(opcode, integers, 2, position)
            else:
                position += 3
        elif opcode.opcode == 7:
            if get_value(opcode, integers, 1, position) < get_value(opcode, integers, 2, position):
                integers[integers[position + 3]] = 1
            else:
                integers[integers[position + 3]] = 0
            position += 4
        elif opcode.opcode == 8:
            if get_value(opcode, integers, 1, position) == get_value(opcode, integers, 2, position):
                integers[integers[position + 3]] = 1
            else:
                integers[integers[position + 3]] = 0
            position += 4
        else:
            raise Exception

        opcode = opcode_decoder(integers[position])

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


if __name__ == "__main__":
    with open("./data/day05.txt") as f:
        data = list(map(int, f.readline().split(",")))

    print("PART ONE")
    print(intcode_calculation(data.copy())[1])

    print("PART TWO")
    print(intcode_calculation(data.copy(), input_id=5)[1])
