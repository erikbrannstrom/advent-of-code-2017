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

def apply_line(line, registers):
	regex = re.compile(r"([a-z]+) ([a-z]+) (-?\d+) if ([a-z]+) ([<>=!]+) (-?\d+)")
	matches = regex.match(line)
	(reg, op, val, reg_comp, comp, val_comp) = matches.groups()
	if operator_to_func(comp)(registers.get(reg_comp, 0), int(val_comp)):
		registers[reg] = operator_to_func(op)(registers.get(reg, 0), int(val))

	return registers


def first(input):
	lines = input.split("\n")
	registers = {}
	for line in lines:
		apply_line(line, registers)

	return max(registers.values())

def second(input):
	lines = input.split("\n")
	registers = {}
	max_value = 0
	for line in lines:
		apply_line(line, registers)
		max_value = max([max_value] + list(registers.values()))

	return max_value