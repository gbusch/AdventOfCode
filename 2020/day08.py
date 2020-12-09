def part1(raw_input):
    """
    >>> part1('''nop +0
    ... acc +1
    ... jmp +4
    ... acc +3
    ... jmp -3
    ... acc -99
    ... acc +1
    ... jmp -4
    ... acc +6''')
    5
    """
    instructions = [(row.split()[0], int(row.split()[1])) for row in raw_input.splitlines()]
    visited_positions = set()
    position = 0
    acc = 0
    i = 0
    while position not in visited_positions:
        visited_positions.add(position)
        position, acc = step(instructions, position, acc)
    return acc

def part2(raw_input):
    """
    >>> part2('''nop +0
    ... acc +1
    ... jmp +4
    ... acc +3
    ... jmp -3
    ... acc -99
    ... acc +1
    ... jmp -4
    ... acc +6''')
    8
    """
    instructions = [(row.split()[0], int(row.split()[1])) for row in raw_input.splitlines()]
    for i, instruction in enumerate(instructions):
        acc = 0
        position = 0
        changed_instructions = instructions.copy()
        if instruction[0] == "nop":
            changed_instructions[i] = ("jmp", instruction[1])
        elif instructions[i][0] == "jmp":
            changed_instructions[i] = ("nop", instruction[1])
        else:
            pass
        visited_positions = set()
        while position < len(instructions):
            visited_positions.add(position)
            position, acc = step(changed_instructions, position, acc)
            if position in visited_positions:
                break
            if position == len(instructions) - 1:
                _, acc = step(changed_instructions, position, acc)
                return acc
    return False

def step(instructions, position, acc):
    """
    >>> instructions = [("nop", 0), ("acc", 2), ("jmp", 2), ("nop", 0)]
    >>> step(instructions, 0, 0)
    (1, 0)
    >>> step(instructions, 1, 0)
    (2, 2)
    >>> step(instructions, 2, 0)
    (0, 0)
    """
    command, num = instructions[position]
    assert command in ["nop", "acc", "jmp"]
    if command == "nop":
        return ((position + 1) % len(instructions), acc)
    elif command == "acc":
        return ((position + 1) % len(instructions), acc + num)
    else:
        return ((position + num) % len(instructions), acc)
    

if __name__ == "__main__":
    with open("./data/day08.txt", "r") as f:
        data = f.read()
    
    print("PART 1")
    print(part1(data))

    print("PART 2")
    print(part2(data))
