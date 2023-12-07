import typing


def load_race_card(filename: str) -> typing.Dict:
    with open(filename, 'r') as fread:
        content = fread.read().split('\n')
        race_card = {}
        for line in content:
            dict_key, dict_values = line.split(":")
            race_card[dict_key] = [int(value) for value in dict_values.strip().split(" ") if value]
    return race_card


def start_the_race(race_time: int, race_distance: int) -> int:
    wins = 0
    for msec in range(1, race_time+1):
        boat_time = race_time - msec
        boat_distance = boat_time * msec

        if boat_distance >= race_distance and boat_time <= race_time:
            # print(f"MSEC: {msec}, Boat time {boat_time}, Race time {race_time}")
            # print(f"MSEC: {msec}, Boat distance {boat_distance}, Race distance {race_distance}")

            if boat_distance == race_distance:
                continue
            wins += 1

    return wins


if __name__ == "__main__":
    race_card = load_race_card("race_card2.txt")

    for race_time, race_distance in zip(race_card["Time"], race_card["Distance"]):
        ways_to_win = start_the_race(race_time, race_distance)
        print(ways_to_win)
