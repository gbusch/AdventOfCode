EXAMPLE_INPUT = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def get_signal_strengths(input_str):
    x = [
        1,
    ]
    for i, line in enumerate(input_str.splitlines()):
        x.append(x[-1])
        if line.startswith("addx"):
            _, step = line.split()
            x.append(x[-1] + int(step))
    return x


def sum_signal_strenghts(X):
    return sum([X[x - 1] * x for x in range(20, 221, 40)])


def print_drawing(X):
    drawing = []
    for i in range(240):
        if i > 0 and i % 40 == 0:
            drawing.append("\n")
        if i % 40 in set(range(X[i] - 1, X[i] + 2)):
            drawing.append("#")
        else:
            drawing.append(".")
    return drawing


X = get_signal_strengths(EXAMPLE_INPUT)
assert X[20 - 1] == 21
assert X[60 - 1] == 19
assert X[100 - 1] == 18
assert X[140 - 1] == 21
assert X[180 - 1] == 16
assert X[220 - 1] == 18, X[55:65]
assert sum_signal_strenghts(X) == 13140

assert (
    "".join(print_drawing(X))
    == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
)


with open("./data/day10.txt", "r") as f:
    data = f.read()

print("part1")
X = get_signal_strengths(data)
print(sum_signal_strenghts(X))

print("part2")
print("".join(print_drawing(X)))
