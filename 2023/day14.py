def part1(input: str) -> int:
    """
    >>> part1('''O....#....
    ... O.OO#....#
    ... .....##...
    ... OO.#O....O
    ... .O.....O#.
    ... O.#..O.#.#
    ... ..O..#O..O
    ... .......O..
    ... #....###..
    ... #OO..#....''')
    136
    """
    return sum(column_load(flip_column("".join(c))) for c in zip(*input.splitlines()))
    

def column_load(column: str) -> int:
    """
    >>> column_load("OO..OO")
    14
    >>> column_load("..OO.#.O.")
    15
    """
    return sum(i+1 for i, s in enumerate(column[::-1]) if s=="O")

def flip_column(column: str) -> str:
    """
    >>> flip_column("OO.O..O.")
    'OOOO....'
    >>> flip_column("..O.O.")
    'OO....'
    >>> flip_column("O.O.#.O.O")
    'OO..#OO..'
    >>> flip_column("O.O.#.O.##")
    'OO..#O..##'
    """
    if "#" in column:
        return "#".join(flip_column(p) for p in column.split("#"))
    count_O = column.count("O")
    return (count_O * "O") + (len(column) - count_O) * "."

if __name__ == "__main__":
    with open("2023/data/day14.txt", "r") as f:
        data = f.read()
    
    print(part1(data))