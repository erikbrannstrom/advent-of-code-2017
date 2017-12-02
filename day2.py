import re

def first(input):
    rows = input.split("\n")

    checksum = 0
    for row in rows:
        string_values = re.split(r'\s', row)
        values = [int(value) for value in string_values]
        checksum = checksum + max(values) - min(values)

    return checksum


def second(input):
    rows = input.split("\n")

    def find_evenly_divisible(values, index):
        for i, value in enumerate(values):
            if index == i or values[index] > value:
                continue
            if (value // values[index]) * values[index] == value:
                return value
        return None

    checksum = 0
    for row in rows:
        string_values = re.split(r'\s', row)
        values = [int(value) for value in string_values]

        for i, value in enumerate(values):
            other = find_evenly_divisible(values, i)
            if other != None:
                checksum = checksum + other // value
                break

    return checksum