def first(input):
	numbers_size = 256
	lengths = [int(i) for i in input.split(",")]
	numbers = list(range(0, numbers_size))
	current_pos = 0
	skip_size = 0

	for length in lengths:
		end_pos = current_pos + length
		sublist = numbers[current_pos:end_pos]
		if end_pos >= numbers_size:
			modulo_end_pos = end_pos % numbers_size
			sublist = sublist + numbers[0:modulo_end_pos]
		sublist = list(reversed(sublist))

		# Append reversed sublist and wrap around if necessary
		numbers[current_pos:current_pos+length] = sublist
		if len(numbers) > numbers_size:
			move_sublist = numbers[numbers_size:]
			numbers = move_sublist + numbers[len(move_sublist):numbers_size]

		current_pos = (current_pos + length + skip_size) % numbers_size
		skip_size = skip_size + 1

	return numbers[0] * numbers[1]
