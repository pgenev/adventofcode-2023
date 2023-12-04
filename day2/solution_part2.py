import typing
from functools import reduce


def load_puzzle(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        return fread.read().split('\n')

def play_the_game(puzzle: typing.List) -> int:
    result = 0
    for row in puzzle:
        game_id, games = row.split(":")
        fewest_number_of_cubes = {}
        for game in games.split(";"):
            game = [g.strip() for g in game.split(",")]
            for cube_combination in game:
                colors_num, color = cube_combination.split(" ")
                if color not in fewest_number_of_cubes or fewest_number_of_cubes[color] < int(colors_num):
                    fewest_number_of_cubes[color] = int(colors_num)

        result += reduce((lambda x, y: x * y), fewest_number_of_cubes.values())
    return result


if __name__ == "__main__":
    puzzle = load_puzzle("puzzle_input.txt")
    result = play_the_game(puzzle)
    print(result)
