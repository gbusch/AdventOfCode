import re
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class GameSet:
    blue: int
    red: int
    green: int

    @classmethod
    def parse_game_set(cls, game_set: str) -> "GameSet":
        """Parse a game set from a string.
        >>> GameSet.parse_game_set('3 blue, 4 red')
        GameSet(blue=3, red=4, green=0)
        >>> GameSet.parse_game_set('1 red, 2 green, 6 blue')
        GameSet(blue=6, red=1, green=2)
        >>> GameSet.parse_game_set('20 green')
        GameSet(blue=0, red=0, green=20)
        """
        colors = defaultdict(int)
        for color in ["blue", "red", "green"]:
            match = re.search(rf"(\d*) {color}", game_set)
            if match:
                colors[color] = int(match.group(1))
        return cls(colors["blue"], colors["red"], colors["green"])


@dataclass
class Game:
    id: int
    game_sets: list[GameSet]

    @classmethod
    def parse_game(cls, game: str) -> "Game":
        """Parse a game from a string.
        >>> Game.parse_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
        Game(id=1, game_sets=[GameSet(blue=3, red=4, green=0), GameSet(blue=6, red=1, green=2), GameSet(blue=0, red=0, green=2)])
        """
        game_name, game_sets_tmp = game.split(":")
        game_id = game_name.split(" ")[1]
        game_sets_tmp = game_sets_tmp.split(";")
        game_sets_tmp = [GameSet.parse_game_set(game_set) for game_set in game_sets_tmp]
        return cls(int(game_id), game_sets_tmp)

    def game_possible(self) -> bool:
        """Check if a game is possible.
        >>> Game.parse_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green').game_possible()
        True
        >>> Game.parse_game('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red').game_possible()
        False
        """
        return all(
            (game_set.red <= 12 and game_set.green <= 13 and game_set.blue <= 14)
            for game_set in self.game_sets
        )

    def find_power(self) -> int:
        """Find the power of a game.
        >>> Game.parse_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green').find_power()
        48
        >>> Game.parse_game('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red').find_power()
        1560
        """
        power = 1
        for color in ["blue", "red", "green"]:
            power *= max(getattr(game_set, color) for game_set in self.game_sets)
        return power


def part1(input: str) -> int:
    """Part 1.
    >>> part1('''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    ... Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    ... Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    ... Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    ... Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green''')
    8
    """
    games = input.split("\n")
    games = [Game.parse_game(game) for game in games]
    return sum(game.id for game in games if game.game_possible())


def part2(input: str) -> int:
    """Part 2.
    >>> part2('''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    ... Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    ... Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    ... Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    ... Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green''')
    2286
    """
    games = input.split("\n")
    games = [Game.parse_game(game) for game in games]
    return sum(game.find_power() for game in games)


if __name__ == "__main__":
    with open("2023/data/day02.txt", "r") as input_file:
        puzzle_input = input_file.read()
    print(part1(puzzle_input))
    print(part2(puzzle_input))
