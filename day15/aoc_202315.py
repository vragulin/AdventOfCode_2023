import pathlib
import sys


def parse(puzzle_input):
	"""Parse input"""
	tokens = puzzle_input.split(",")
	return tokens


def my_hash(inp: str) -> int:
	h = 0
	for c in inp:
		h += ord(c)
		h *= 17
		h = h % 256
	return h


def parse_mirror(inp: str) -> tuple:
	if '=' in inp:
		label, strength = inp.split('=')
		strength = int(strength)
	elif '-' in inp:
		label = inp[:-1]
		strength = None
	else:
		print("Warning: can't parse ", inp)
	return label, strength


def part1(data):
	"""Solve part 1"""
	sum_all = 0
	for token in data:
		sum_all += my_hash(token)

	return sum_all


def part2(data):
	"""Solve part 2"""
	boxes = {}
	for token in data:
		label, strength = parse_mirror(token)
		box_i = my_hash(label)
		if strength:  # Operator =
			same_label_found = False
			if box_i in boxes:
				for j, lens in enumerate(boxes[box_i]):
					if lens[0] == label:
						boxes[box_i][j][1] = strength
						same_label_found = True
						break
				if not same_label_found:
					boxes[box_i].append([label, strength])
			else:
				boxes[box_i] = [[label, strength]]
		else:  # Operator -
			if box_i in boxes:
				for j, lens in enumerate(boxes[box_i]):
					if lens[0] == label:
						boxes[box_i].pop(j)

	# Calc final result
	sum_all = 0
	for i, box in boxes.items():
		for j, lens in enumerate(box):
			sum_all += (i + 1) * (j + 1) * lens[1]

	return sum_all


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
