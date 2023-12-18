import pathlib
import sys
import numpy as np


def parse(puzzle_input):
	"""  Read puzzle input
	:param puzzle_input:
	:return:
	"""
	lines = puzzle_input.split('\n')
	data = []
	current_block = []
	for line in lines:
		if len(line) == 0:
			if len(current_block) > 0:
				data.append(current_block)
				current_block = []
		else:
			current_block.append(list(line.strip()))

	if len(current_block) > 0:
		data.append(current_block)

	return data


def check_symmetry(array, pos):
	# Pos - testing if there is a symmetry before element #pos
	n = len(array)
	if pos == 0 | pos >= n:
		return False
	dist = 0
	while (pos - dist > 0) and (pos + dist < n):
		if array[pos - dist - 1] != array[pos + dist]:
			return False
		dist += 1
	return True


def find_all_row_symmetries(array2d):
	ncols = len(array2d[0])
	# symmetry_list = [x for x in range(1, ncols) if np.abs(x - ncols / 2.0) < 1]
	symmetry_list = list(range(1, ncols))
	for i, row in enumerate(array2d):
		for j, sym in enumerate(symmetry_list):
			if not check_symmetry(row, sym):
				symmetry_list.pop(j)
				if len(symmetry_list) == 0:
					break
	return symmetry_list


def find_all_col_symmetries(array2d):
	nrows = len(array2d)
	ncols = len(array2d[0])
	# symmetry_list = [x for x in range(1, nrows) if np.abs(x - nrows / 2.0) < 1]
	symmetry_list = list(range(1, nrows))
	for j in range(ncols):
		for k, sym in enumerate(symmetry_list):
			col = [array2d[i][j] for i in range(len(array2d))]
			if not check_symmetry(col, sym):
				symmetry_list.pop(k)
				if len(symmetry_list) == 0:
					break
	return symmetry_list


def part1(data):
	"""Solve part 1"""
	sum_row = 0
	sum_col = 0

	for tab in data:
		row_sym = find_all_row_symmetries(tab)
		if len(row_sym) > 0:
			sum_row += row_sym[0]
		else:
			col_sym = find_all_col_symmetries(tab)
			if len(col_sym) > 0:
				sum_col += col_sym[0]

	return 100 * sum_col + sum_row


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
