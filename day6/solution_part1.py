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
    wins = []
    for msec in range(1, race_time+1):
        boat_time = race_time - msec
        boat_distance = boat_time * msec

        if boat_distance >= race_distance and boat_time <= race_time:
            print(f"MSEC: {msec}, Boat time {boat_time}, Race time {race_time}")
            print(f"MSEC: {msec}, Boat distance {boat_distance}, Race distance {race_distance}")

            if boat_distance == race_distance:
                continue
            wins.append(msec)

    return len(wins)


if __name__ == "__main__":
    race_card = load_race_card("race_card.txt")
    num_of_ways_to_beat_the_record = None
    for race_time, race_distance in zip(race_card["Time"], race_card["Distance"]):
        ways = start_the_race(race_time, race_distance)
        if not num_of_ways_to_beat_the_record:
            num_of_ways_to_beat_the_record = ways
            continue
        num_of_ways_to_beat_the_record *= ways

    print(num_of_ways_to_beat_the_record)
