import typing

BAG = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def load_puzzle(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        return fread.read().split('\n')

def play_the_game(puzzle: typing.List) -> int:
    possible_games = 0
    for row in puzzle:
        possible_game = True
        game_id, games = row.split(":")
        for game in games.split(";"):
            if possible_game is False:
                break
            game = [g.strip() for g in game.split(",")]
            combinations = {}
            for cube_combination in game:
                colors_num, color = cube_combination.split(" ")
                if color not in combinations:
                    combinations[color] = int(colors_num)
                else:
                    combinations[color] += int(colors_num)
            for color, color_num in combinations.items():
                if BAG[color] < color_num:
                    possible_game = False
                    break
        if possible_game:
            game_id = int(game_id.split(" ")[-1])
            possible_games += game_id
    return possible_games


if __name__ == "__main__":
    puzzle = load_puzzle("puzzle_input.txt")
    possible_games = play_the_game(puzzle)
    print(possible_games)
