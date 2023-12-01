import typing

def load_calibration_map(filename: str) -> typing.List:
    with open(filename, 'r') as fread:
        return fread.read().split('\n')

def calculate_calibration_value(calibration_map: typing.List) -> int:
    calibration_value = 0
    for line in calibration_map:
        first_digit =  next((char for char in line if char.isdigit()), 0)
        last_digit = next((char for char in line[::-1] if char.isdigit()), 0)
        calibration_value += int(f"{first_digit}{last_digit}")
    return calibration_value


if __name__ == "__main__":
    calibration_map = load_calibration_map("calibration_document")
    calibration_value = calculate_calibration_value(calibration_map)
    print(calibration_value)
