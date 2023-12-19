import pathlib
import sys
from collections import namedtuple


def parse(puzzle_input) -> dict:
	"""Parse input"""
	lines = puzzle_input.split()
	instructions = {}
	parts = []
	first_workflow = "in"
	# Read instructions
	counter = 0
	while (line := lines[counter])[0] != "{":
		workflow, rest = line.split("{")
		counter += 1
		tokens = rest[:-1].split(",")
		instructions[workflow] = []
		for token in tokens:
			if ':' not in token:
				token_dict = {'action': token}
			else:
				condition, action = token.split(':')
				for op in ['<', '>']:
					if op in condition:
						feature, value = condition.split(op)
						token_dict = {'condition': (feature, op, int(value)),
						              'action': action}
						break
			instructions[workflow].append(token_dict)

	# Read parts
	for line in lines[counter:]:
		tokens = line[1:-1].split(",")
		item = {}
		for token in tokens:
			feature, num = token.split('=')
			item[feature] = int(num)
		assert ('x' in item) and ('m' in item) and ('a' in item) \
		       and ('s' in item), "Missing item info"
		parts.append(item)

	return {'inst': instructions, 'parts': parts, 'first': first_workflow}


def next_workflow(part: dict, workflow: str, data: dict) -> str:
	rules = data['inst'][workflow]
	for rule in rules:
		if 'condition' not in rule:
			return rule['action']
		else:
			feature, op, value = rule['condition']
			if part[feature] > value if op == ">" else part[feature] < value:
				return rule['action']
	raise ValueError("Ran out of rules: " + str(rules))


def check_final_state(part, data):
	workflow = data['first']
	while workflow not in ['A', 'R']:
		workflow = next_workflow(part, workflow, data)
	return True if workflow == 'A' else False


def part1(data):
	"""Solve part 1"""
	sum_all = 0
	for part in data['parts']:
		# A = True, R = False
		if check_final_state(part, data):
			for feature in part:
				sum_all += part[feature]
	return sum_all


def part2(data):
	"""Solve part 2"""


def solve(puzzle_input):
	"""Solve the puzzle for the given input"""
	data = parse(puzzle_input)
	solution1 = part1(data)
	solution2 = part2(data)

	return solution1, solution2


if __name__ == "__main__":
	for path in sys.argv[1:]:
		print(f"{path}:")
		puzzle_input = pathlib.Path(path).read_text().strip()
		solutions = solve(puzzle_input)
		print("\n".join(str(solution) for solution in solutions))
