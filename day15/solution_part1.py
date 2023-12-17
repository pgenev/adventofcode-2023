import typing


def load_sequence(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        lines = fread.read().split('\n')
        return [line for line in lines[0].split(",") if line]


def hash_algorithm(sub_sequence: str) -> int:
    current_value = None
    for char in sub_sequence:
        if not current_value:
            current_value = ord(char) * 17
            current_value %= 256
            continue
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


if __name__ == "__main__":
    sequence = load_sequence("sequence.txt")
    results = sum(hash_algorithm(sub_sequnce) for sub_sequnce in sequence)
    print(results)



