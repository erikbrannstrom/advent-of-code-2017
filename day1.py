def first(input):
    sum = 0
    for i in range(len(input)):
        next = (i + 1) % len(input)
        if input[i] == input[next]:
            sum = sum + int(input[i])
    return sum


def second(input):
    sum = 0
    for i in range(len(input)):
        next = (i + (len(input) // 2)) % len(input)
        if input[i] == input[next]:
            sum = sum + int(input[i])
    return sum