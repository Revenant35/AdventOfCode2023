from util.read_file import read_file
import numpy as np


digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def get_first_digit(content, use_strings=False):
    first_digit = None
    first_digit_index = len(content)
    for digit in digits.values():
        found = content.find(str(digit), 0, first_digit_index+1)
        if found != -1:
            first_digit = digit
            first_digit_index = found
    if use_strings:
        for digit_string, digit_value in digits.items():
            found = content.find(digit_string, 0, first_digit_index+1)
            if found != -1:
                first_digit = digit_value
                first_digit_index = found + len(digit_string) - 1

    return first_digit


def get_last_digit(content, use_strings=False):
    last_digit = None
    last_digit_index = 0
    for digit in digits.values():
        found = content.rfind(str(digit), last_digit_index, len(content))
        if found != -1:
            last_digit = digit
            last_digit_index = found

    if use_strings:
        for digit_string, digit_value in digits.items():
            found = content.rfind(digit_string, last_digit_index, len(content))
            if found != -1:
                last_digit = digit_value
                last_digit_index = found + len(digit_string) - 1

    return last_digit


def main(input_filepath):
    contents = read_file(input_filepath)
    contents = contents.split("\n")

    part_one = np.sum([(10 * get_first_digit(line, use_strings=False)) + get_last_digit(line, use_strings=False) for line in contents])
    part_two = np.sum([(10 * get_first_digit(line, use_strings=True)) + get_last_digit(line, use_strings=True) for line in contents])

    assert part_one == 53194  # Verified solution
    assert part_two == 54249  # Verified solution

    print(f"Day 1 Part 1: {part_one}")
    print(f"Day 1 Part 2: {part_two}")


if __name__ == '__main__':
    main("./input.txt")
