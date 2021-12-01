import pandas as pd


def part1(inlist: list[int]) -> int:
    """
    >>> inlist = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    >>> part1(inlist)
    7
    """
    df = pd.DataFrame({"in": inlist})
    df["shift"] = df["in"].shift(1)
    df["diff"] = df["in"] - df["shift"]
    df["increase"] = df["diff"] > 0
    return df["increase"].sum()


def part2(inlist: list[int], window: int) -> int:
    """
    >>> inlist = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    >>> part2(inlist, 3)
    5
    """
    df = pd.DataFrame({"in": inlist})
    newlist = list(df.rolling(window).sum()["in"])
    return part1(newlist)


if __name__ == "__main__":
    with open("data/day01.txt", "r") as f:
        inlist = [int(x) for x in f.read().split()]

    print(f"Part 1: {part1(inlist)}")
    print(f"Part 2: {part2(inlist, 3)}")
