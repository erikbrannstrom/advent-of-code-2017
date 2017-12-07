def is_valid_line(line):
    words = line.split()
    return len(words) == len(set(words))

def first(input):
    lines = input.split("\n")
    return len([line for line in lines if is_valid_line(line)])