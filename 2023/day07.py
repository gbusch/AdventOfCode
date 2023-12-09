from collections import Counter


def main(input: str, joker: bool = False) -> int:
    """Part 1
    >>> main('''32T3K 765
    ... T55J5 684
    ... KK677 28
    ... KTJJT 220
    ... QQQJA 483''')
    6440
    >>> main('''32T3K 765
    ... T55J5 684
    ... KK677 28
    ... KTJJT 220
    ... QQQJA 483''', joker=True)
    5905
    """
    return sum(
        int(hand[1]) * (rank + 1)
        for rank, hand in enumerate(
            sorted(
                [hand.split() for hand in input.splitlines()],
                key=lambda x: score_hand(x[0], joker),
            )
        )
    )


def score_hand(hand: str, joker: bool = False) -> int:
    """Returns the score of hand
    >>> score_hand("AAAAA")
    6978670
    >>> score_hand("AJAAJ", joker=False)
    4966379
    >>> score_hand("AJAAJ", joker=True)
    6925409
    >>> score_hand("AA8AA")
    5977134
    >>> score_hand("23456")
    144470
    """
    return score_type(hand, joker) * 1000000 + score_strength(hand, joker)


def score_type(hand: str, joker: bool = False) -> int:
    """Returns the type of hand
    >>> score_type("AAAAA")
    6
    >>> score_type("AAJJA", joker=True)
    6
    >>> score_type("AA8AA")
    5
    >>> score_type("23332")
    4
    >>> score_type("TTT98")
    3
    >>> score_type("23432")
    2
    >>> score_type("A23A4")
    1
    >>> score_type("23456")
    0
    """

    def simple_score(hand: str) -> int:
        counts = Counter(hand)
        if len(counts) == 1:
            return 6
        elif len(counts) == 2:
            return 5 if 4 in counts.values() else 4
        elif len(counts) == 3:
            return 3 if 3 in counts.values() else 2
        elif len(counts) == 4:
            return 1
        else:
            return 0

    if joker:
        return max(simple_score(hand.replace("J", card)) for card in "23456789TQKA")
    return simple_score(hand)


def score_strength(hand: str, joker: bool = False) -> int:
    """Returns the strength of hand
    >>> score_strength("AAAAA")
    978670
    >>> score_strength("AA8TT")
    977066
    >>> score_strength("23456")
    144470
    >>> score_strength("JJJJ5", joker=False)
    768949
    >>> score_strength("JJJJ5", joker=True)
    69909
    """
    hand_hex = (
        hand.replace("A", "E")
        .replace("T", "A")
        .replace("J", "1" if joker else "B")
        .replace("Q", "C")
        .replace("K", "D")
    )
    return int(hand_hex, 16)


if __name__ == "__main__":
    with open("2023/data/day07.txt") as file:
        input = file.read()
    print(main(input))
    print(main(input, joker=True))
