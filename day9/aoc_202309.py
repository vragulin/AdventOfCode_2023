import pathlib
import sys
import numpy as np


def parse(puzzle_input) -> list:
	"""Parse input"""
	lines = puzzle_input.split('\n')
	s_list = []
	for line in lines:
		series = [int(x) for x in line.split()]
		s_list.append(series)
	return s_list


def part1_with_np(data):
	"""Solve part 1"""
	sum_pred = 0
	for s in data:
		n = len(s)
		x = np.arange(n)
		y = np.array(s)
		z = np.polyfit(x, y, n - 1)
		pred = np.round(np.polyval(z, n))
		sum_pred += pred
	return sum_pred


def extrap(s: list) -> int:
	n = len(s)
	diff = s
	last_elm = []  # List of the last element in each diff series
	while not all(v == 0 for v in diff):
		diff = [diff[i + 1] - diff[i] for i in range(len(diff) - 1)]
		last_elm.append(diff[-1])

	# Build the projection
	res = s[-1] + sum(last_elm)
	return res


def extrap_back(s: list) -> int:
	n = len(s)
	diff = s
	first_elm = []  # List of the last element in each diff series
	while not all(v == 0 for v in diff):
		diff = [diff[i + 1] - diff[i] for i in range(len(diff) - 1)]
		first_elm.append(diff[0])

	# Build the projection
	res = s[0] - sum(first_elm[i] * (-1) ** i for i in range(len(first_elm) - 1))
	return res


def part1(data):
	"""Solve part 1"""
	sum_pred = 0
	for s in data:
		sum_pred += extrap(s)
	return sum_pred


def part2(data):
	"""Solve part 2"""
	sum_pred = 0
	for s in data:
		sum_pred += extrap_back(s)
	return sum_pred


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
