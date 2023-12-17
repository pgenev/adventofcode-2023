import typing


def load_sequence(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        lines = fread.read().split('\n')
        return [line for line in lines[0].split(",") if line]


def hash_algorithm(sub_sequence: str) -> int:
    box_number = None
    new_sequence = []
    for char in sub_sequence:
        if char in ("=", "-"):
            if char == "-":
                new_sequence.append(char)
            continue
        if char.isdigit():
            new_sequence.append(char)
            continue
        if not box_number:
            box_number = ord(char) * 17
            box_number %= 256
            new_sequence.append(char)
            continue
        box_number += ord(char)
        box_number *= 17
        box_number %= 256
        new_sequence.append(char)

    return box_number, "".join(new_sequence)


if __name__ == "__main__":
    sequence = load_sequence("sequence.txt")
    boxes = {}
    for sub_sequence in sequence:
        box_number, label = hash_algorithm(sub_sequence)
        if box_number not in boxes:
            if not label.endswith("-"):
                boxes[box_number] = [label]
            continue
        box_labels = boxes[box_number]
        for ind, box_label in enumerate(box_labels):
            if label.endswith("-"):
                box_value_without_dash = label.split("-")[0]
                if box_value_without_dash == box_label[:-1]:
                    box_labels.pop(ind)
                    if not box_labels:
                        del boxes[box_number]
                    break
            else:
                box_value_without_num = label[:-1]
                box_values_without_numbers = [bl[:-1] for bl in box_labels]
                if box_value_without_num not in box_values_without_numbers:
                    box_labels.append(label)
                else:
                    box_v_ind = box_values_without_numbers.index(box_value_without_num)
                    box_labels[box_v_ind] = label
                break
    results = 0
    for box_num, lenses in boxes.items():
        box_num += 1
        for slot, lens in enumerate(lenses):
            slot += 1
            results += box_num*slot*int(lens[-1])

    print(results)








