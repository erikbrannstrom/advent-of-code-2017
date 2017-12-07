def first(input):
    def is_valid_line(line):
        words = line.split()
        return len(words) == len(set(words))

    lines = input.split("\n")
    return len([line for line in lines if is_valid_line(line)])

def second(input):
    def word_to_dict(word):
        result = {}
        for c in word:
            result[c] = result.get(c, 0) + 1
        return result

    def is_valid_line(line):
        word_dicts = [word_to_dict(word) for word in line.split()]
        for wd in word_dicts:
            if word_dicts.count(wd) > 1:
                return False
        return True

    lines = input.split("\n")
    return len([line for line in lines if is_valid_line(line)])