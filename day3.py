DIRECTION = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def first(input):
    square = int(input)
    coords = (0, 0)

    dir_index = 0
    steps_until_increase = 2
    steps_taken = 0
    for current_square in range(1, square):
        coords = (coords[0] + DIRECTION[dir_index][0],
                  coords[1] + DIRECTION[dir_index][1])

        steps_taken = steps_taken + 1
        if steps_taken == steps_until_increase / 2:
            dir_index = (dir_index + 1) % 4
        if steps_taken == steps_until_increase:
            dir_index = (dir_index + 1) % 4
            steps_until_increase = steps_until_increase + 2
            steps_taken = 0

    return abs(coords[0]) + abs(coords[1])


def second(input):
    val = int(input)
    max_value = 1
    matrix_dict = {
        (0, 0): 1
    }
    coords = (0, 0)

    def sum_neighbors(coords):
        return sum([matrix_dict.get((coords[0] + 1, coords[1] + 1), 0),
            matrix_dict.get((coords[0] + 1, coords[1]), 0),
            matrix_dict.get((coords[0] + 1, coords[1] - 1), 0),
            matrix_dict.get((coords[0], coords[1] + 1), 0),
            matrix_dict.get((coords[0], coords[1] - 1), 0),
            matrix_dict.get((coords[0] - 1, coords[1] + 1), 0),
            matrix_dict.get((coords[0] - 1, coords[1]), 0),
            matrix_dict.get((coords[0] - 1, coords[1] - 1), 0)])

    dir_index = 0
    steps_until_increase = 2
    steps_taken = 0
    current_square = 1
    while max_value <= val:
        coords = (coords[0] + DIRECTION[dir_index][0],
                  coords[1] + DIRECTION[dir_index][1])

        matrix_dict[coords] = sum_neighbors(coords)
        max_value = matrix_dict[coords]

        steps_taken = steps_taken + 1
        if steps_taken == steps_until_increase / 2:
            dir_index = (dir_index + 1) % 4
        if steps_taken == steps_until_increase:
            dir_index = (dir_index + 1) % 4
            steps_until_increase = steps_until_increase + 2
            steps_taken = 0

    return max_value
