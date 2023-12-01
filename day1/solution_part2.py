import typing

def load_calibration_map(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        return fread.read().split('\n')

def calculate_calibration_value(calibration_map: typing.List) -> int:
    calibration_value = 0
    for line in calibration_map:
        first_digit = find_digit(line)
        last_digit = find_digit(line, -1)
        print(f"{first_digit}{last_digit}")
        calibration_value += int(f"{first_digit}{last_digit}")
    return calibration_value

def find_digit(line: str, reverse: int = 1) -> str:
    valid_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    valid_digit = ""
    for char in line[::reverse]:
        if digit := [digit for digit in valid_digits if digit in valid_digit[::reverse]]:
            return valid_digits[digit[0]]
        elif char.isdigit():
            return char
        else:
            valid_digit += char



if __name__ == "__main__":
    calibration_map = load_calibration_map("calibration_document")
    calibration_value = calculate_calibration_value(calibration_map)
    print(calibration_value)
