import typing

def load_scrachcards(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        return fread.read().split('\n')

def start_scratching(scratchcards: typing.List) -> int:
    total_points = 0
    for card in scratchcards:
        _, all_numbers = card.split(":")
        winning_numbers, my_numbers = all_numbers.split("|")
        winning_numbers = {int(win_num) for win_num in winning_numbers.split(" ") if win_num.isdigit()}
        my_numbers = {int(my_num) for my_num in my_numbers.split(" ") if my_num.isdigit()}
        matches = winning_numbers.intersection(my_numbers)
        points = 0
        for index, match in enumerate(matches):
            if index == 0:
                points = 1
                continue
            points *= 2

        total_points += points
    return total_points




if __name__ == "__main__":
    scratchcards = load_scrachcards("scratchcards.txt")
    total_points = start_scratching(scratchcards)
    print(total_points)