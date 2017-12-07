def get_coordinates(square):
    coords = (0, 0)

    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_index = 0
    steps_until_increase = 2
    steps_taken = 0
    for current_square in range(1, square):
        coords = (coords[0] + direction[dir_index][0],
                  coords[1] + direction[dir_index][1])

        steps_taken = steps_taken + 1
        if steps_taken == steps_until_increase / 2:
            dir_index = (dir_index + 1) % 4
        if steps_taken == steps_until_increase:
            dir_index = (dir_index + 1) % 4
            steps_until_increase = steps_until_increase + 2
            steps_taken = 0

    return coords


def first(input):
    square = int(input)
    coords = get_coordinates(square)
    return abs(coords[0]) + abs(coords[1])
