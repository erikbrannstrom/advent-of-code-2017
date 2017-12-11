MOVEMENT = {
	"nw": (-0.5, 0.5),
	"n": (0, 1),
	"ne": (0.5, 0.5),
	"se": (0.5, -0.5),
	"s": (0, -1),
	"sw": (-0.5, -0.5)
}

def move(coords, step):
	move = MOVEMENT[step]
	return (coords[0] + move[0], coords[1] + move[1])

def distance(coords):
	diagonal_steps = abs(coords[0]) * 2
	straight_steps = abs(coords[1]) - diagonal_steps * 0.5
	return diagonal_steps + straight_steps

def first(input):
	steps = input.split(",")
	coords = (0,0)

	for step in steps:
		coords = move(coords, step)

	return distance(coords)

def second(input):
	steps = input.split(",")
	coords = (0,0)
	max_distance = 0

	for step in steps:
		coords = move(coords, step)
		max_distance = max(max_distance, distance(coords))

	return max_distance
