import typing


def load_almanac(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        return fread.read().split('\n')


def convert_almanac_as_dict(almanac: typing.List) -> typing.Dict:
    almanac_dict = {}
    for row in almanac:
        if ":" in row:
            my_key = row.replace(":", "")
            section = my_key.strip()
        elif section in almanac_dict:
            almanac_dict[section] += [[int(value) for value in row.strip().split()]] if row else []
        else:
            almanac_dict[section] = [[int(value) for value in row.strip().split()]] if row else []
    return almanac_dict

def find_lowest_location_number(almanac_dict, seed: int) -> int:
    steps_order = (
        "seed-to-soil map",
        "soil-to-fertilizer map",
        "fertilizer-to-water map",
        "water-to-light map",
        "light-to-temperature map",
        "temperature-to-humidity map",
        "humidity-to-location map"
    )
    target = seed
    for section in steps_order:
        values = almanac_dict[section]
        corresponding_values = []
        for value in values:
            range_length = value[-1]
            destination_range_start = range(value[0], value[0]+range_length)
            source_range_start = range(value[1], value[1]+range_length)
            for combination in zip(destination_range_start, source_range_start):
                if target == combination[-1]:
                    corresponding_values.append(combination)

        for combination in corresponding_values:
            if target == combination[-1]:
                target = combination[0]
                break
    return target


if __name__ == "__main__":
    almanac = load_almanac("almanac.txt")
    almanac_dict = convert_almanac_as_dict(almanac)
    seeds = almanac_dict.pop("seeds")[0]
    lowest_location_number = None

    for seed in seeds:
        location_number = find_lowest_location_number(almanac_dict, seed)
        if not lowest_location_number or lowest_location_number > location_number:
            lowest_location_number = location_number
    print(location_number)
