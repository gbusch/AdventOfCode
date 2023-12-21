def part1(input: str) -> str:
    """
    >>> part1('''>|<<<\....
    ... |v-.\^....
    ... .v...|->>>
    ... .v...v^.|.
    ... .v...v^...
    ... .v...v^..\
    ... .v../2\\..
    ... <->-/vv|..
    ... .|<<<2-|.\
    ... .v//.|.v..''')
    46
    """
    contraption = parse_contraption(input)
    



def light_react(direction: str, object: str) -> str:
    """
    >>> light_react("R", ".")
    ['R']
    >>> light_react("R", "/")
    ['U']
    >>> light_react("R", "\\\\")
    ['D']
    >>> light_react("R", "|")
    ['D', 'U']
    >>> light_react("R", "-")
    ['R']
    """
    match object:
        case ".":
            return [direction]
        case "/":
            match direction:
                case "R":
                    return ["U"]
                case "L":
                    return ["D"]
                case "U":
                    return ["R"]
                case "D":
                    return ["L"]
        case "\\":
            match direction:
                case "R":
                    return ["D"]
                case "L":
                    return ["U"]
                case "U":
                    return ["L"]
                case "D":
                    return ["R"]
        case "|":
            match direction:
                case "R":
                    return ["D", "U"]
                case "L":
                    return ["D", "U"]
                case "U":
                    return ["U"]
                case "D":
                    return ["D"]
        case "-":
            match direction:
                case "R":
                    return ["R"]
                case "L":
                    return ["L"]
                case "U":
                    return ["L", "R"]
                case "D":
                    return ["L", "R"]
                
def parse_contraption(input: str) -> dict[tuple[int, int], str]:
    """
    >>> parse_contraption("/-\|")
    {(0, 0): '/', (1, 0): '-', (2, 0): '\\\\', (3, 0): '|'}
    """
    contraption = {}
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            contraption[(x, y)] = char
    return contraption