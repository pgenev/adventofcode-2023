import typing


def load_map(filename: str) -> (str, typing.Dict):
    with open(filename, 'r') as fread:
        instructions_map = fread.read().split('\n')
        instructions, *instructions_map = instructions_map
        map_dict = {}
        for instruction in instructions_map:
            if instruction:
                k, v = instruction.split("=")
                k = k.strip()
                v1, v2 = v.strip().split(",")
                v1 = v1.strip("(").strip()
                v2 = v2.strip(")").strip()
                if k not in map_dict:
                    map_dict[k] = (v1, v2)

    return instructions, map_dict


def reach_zzz(instructions: str, map_dict: typing.Dict) -> int:
    steps = 0
    instructions_copy = instructions
    instructions = list(instructions)
    found_sequence = None

    while instructions:
        direction = instructions.pop(0)
        if not found_sequence:
            found_sequence = map_dict.get("AAA")
            steps += 1
            if direction == "L":
                found_item = found_sequence[0]
            elif direction == "R":
                found_item = found_sequence[-1]
            if found_item == "ZZZ":
                break
            continue

        found_sequence = map_dict.get(found_item)
        steps += 1

        if direction == "L":
            found_item = found_sequence[0]
        elif direction == "R":
            found_item = found_sequence[-1]
        if found_item == "ZZZ":
            break
        elif instructions:
            continue
        else:
            instructions = list(instructions_copy)
    return steps


if __name__ == "__main__":
    instructions, map_dict = load_map("map.txt")
    steps = reach_zzz(instructions, map_dict)
    print(steps)

