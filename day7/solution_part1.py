import typing
import copy


CARDS_STRENGTH = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
HAND_STRENGTH_ORDER = (
        "High card",
        "One pair",
        "Two pair",
        "Three of a kind",
        "Full house",
        "Four of a kind",
        "Five of a kind",
    )


def load_cards(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        return fread.read().split('\n')


def type_of_card(card) -> str:
    card_labels = {}
    for char in card:
        if char in card_labels:
            card_labels[char] += 1
        else:
            card_labels[char] = 1

    card_values = list(card_labels.values())

    if card_values.count(5) == 1:
        return HAND_STRENGTH_ORDER[6]
    elif card_values.count(4) == 1:
        return HAND_STRENGTH_ORDER[5]
    elif card_values.count(3) == 1 and card_values.count(1) == 2:
        return HAND_STRENGTH_ORDER[3]
    elif card_values.count(3) == 1:
        return HAND_STRENGTH_ORDER[4]
    elif card_values.count(2) == 2:
        return HAND_STRENGTH_ORDER[2]
    elif card_values.count(2) == 1:
        return HAND_STRENGTH_ORDER[1]
    elif card_values.count(1) == 5:
        return HAND_STRENGTH_ORDER[0]


def process_total_winnings(cards: typing.List) -> int:
    cards_type = {}
    for card in cards:
        card, bid_amount = card.split(" ")
        card_type = type_of_card(card)
        if card_type not in cards_type:
            cards_type[card_type] = [(card, bid_amount)]
        else:
            cards_type[card_type].append((card, bid_amount))

    rank = 1
    total_winnings = 0

    for card_strength in HAND_STRENGTH_ORDER:
        if cards_type.get(card_strength):
            if len(cards_type.get(card_strength)) == 1:
                total_winnings += int(cards_type.get(card_strength)[0][-1]) * rank
                cards_type.get(card_strength).pop(0)
                rank += 1
            else:
                cards_order = []
                cards_order_copy = []

                while cards_type.get(card_strength):
                    card_type = cards_type.get(card_strength).pop(0)
                    if not cards_order:
                        cards_order.append(card_type)
                        continue

                    cards_order_copy = copy.deepcopy(cards_order)
                    new_card_position = 0

                    break_outer_loop = False
                    for position, hand in enumerate(cards_order_copy):
                        for char1, char2 in zip(hand[0], card_type[0]):
                            if CARDS_STRENGTH.index(char2) > CARDS_STRENGTH.index(char1):
                                new_card_position = new_card_position + position + 1
                                break
                            elif CARDS_STRENGTH.index(char2) < CARDS_STRENGTH.index(char1):
                                new_card_position = position
                                break_outer_loop = True
                                break
                        if break_outer_loop:
                            break
                    cards_order.insert(new_card_position, card_type)


                for card, bid in cards_order:
                    total_winnings = total_winnings + (int(bid) * rank)
                    rank += 1

    return total_winnings


if __name__ == "__main__":
    cards = load_cards("cards.txt")
    total_winnings = process_total_winnings(cards)
    print(total_winnings)

