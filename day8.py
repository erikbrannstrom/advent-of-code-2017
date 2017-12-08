import re

def operator_to_func(op):
	operators = {
		">": lambda x, y: x > y,
		">=": lambda x, y: x >= y,
		"<": lambda x, y: x < y,
		"<=": lambda x, y: x <= y,
		"==": lambda x, y: x == y,
		"!=": lambda x, y: x != y,
		"inc": lambda x, y: x + y,
		"dec": lambda x, y: x - y
	}
	return operators.get(op)

def first(input):
	regex = re.compile(r"([a-z]+) ([a-z]+) (-?\d+) if ([a-z]+) ([<>=!]+) (-?\d+)")

	lines = input.split("\n")
	registers = {}
	for line in lines:
		matches = regex.match(line)
		(reg, op, val, reg_comp, comp, val_comp) = matches.groups()

		if not operator_to_func(comp)(registers.get(reg_comp, 0), int(val_comp)):
			continue

		registers[reg] = operator_to_func(op)(registers.get(reg, 0), int(val))

	return max(registers.values())