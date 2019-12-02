def intcode_calculation(integers):
    """
    Intcode program.
    >>> intcode_calculation([1, 0, 0, 0, 99])
    [2, 0, 0, 0, 99]
    >>> intcode_calculation([2, 3, 0, 3, 99])
    [2, 3, 0, 6, 99]
    >>> intcode_calculation([2, 4, 4, 5, 99, 0])
    [2, 4, 4, 5, 99, 9801]
    >>> intcode_calculation([1, 1, 1, 4, 99, 5, 6, 0, 99])
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    """
    position = 0
    opcode = integers[position]

    while opcode != 99:
        left_inp_pos = integers[position+1]
        right_inp_pos = integers[position+2]
        outp_pos = integers[position+3]

        if opcode == 1:
            integers[outp_pos] = integers[left_inp_pos] + integers[right_inp_pos]
        elif opcode == 2:
            integers[outp_pos] = integers[left_inp_pos] * integers[right_inp_pos]
        else:
            raise Exception

        position += 4
        opcode = integers[position]

    return integers


def run_with_input(integers, noun, verb):
    integers_input = integers.copy()
    integers_input[1] = noun
    integers_input[2] = verb
    return intcode_calculation(integers_input)


with open("./data/day02.txt") as f:
    data = f.read().split(",")

integers = list(map(int, data))

print("PART ONE")
solution_part1 = run_with_input(integers, 12, 2)[0]
print(solution_part1)
assert solution_part1 == 5434663

print("PART TWO")
for noun in range(100):
    for verb in range(100):
        result = run_with_input(integers, noun, verb)[0]
        if result == 19690720:
            print(noun, verb, noun*100+verb)
