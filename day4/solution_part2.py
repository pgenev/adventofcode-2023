import typing

def load_scrachcards(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        return fread.read().split('\n')

def start_scratching(scratchcards: typing.List) -> int:
    card_dict = {}
    for card in scratchcards:
        current_card, all_numbers = card.split(":")
        card_number = int(current_card.split(" ")[-1])
        winning_numbers, my_numbers = all_numbers.split("|")
        winning_numbers = {int(win_num) for win_num in winning_numbers.split(" ") if win_num.isdigit()}
        my_numbers = {int(my_num) for my_num in my_numbers.split(" ") if my_num.isdigit()}
        matches = winning_numbers.intersection(my_numbers)
        if f"Card {card_number}" not in card_dict:
            card_dict[f"Card {card_number}"] = 1
        else:
            card_dict[f"Card {card_number}"] += 1
        index_2 = 1
        foo = len(matches)
        while foo:
            if f"Card {card_number+index_2}" not in card_dict:
                card_dict[f"Card {card_number+index_2}"] = 0
            index_2 += 1
            foo -= 1
        index = 1
        while len(matches):
            if f"Card {card_number+index}" not in card_dict:
                card_dict[f"Card {card_number+index}"] = 1
            else:
                card_dict[f"Card {card_number+index}"] += card_dict[f"Card {card_number}"]
            index += 1
            matches.pop()


    return sum(card_dict.values())


if __name__ == "__main__":
    scratchcards = load_scrachcards("scratchcards.txt")
    total_scratchcards = start_scratching(scratchcards)
    print(total_scratchcards)