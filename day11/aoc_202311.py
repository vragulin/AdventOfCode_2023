import copy
import pathlib
import sys
from itertools import combinations

EXPAND_FACTOR1 = 2
EXPAND_FACTOR2 = 1_000_000


def parse(puzzle_input):
	"""Parse input"""
	lines = puzzle_input.split('\n')
	galaxies = []
	for x, line in enumerate(lines):
		series = list(line)
		for y, s in enumerate(series):
			if s == '#':
				galaxies.append([x, y])
	galaxies.sort()
	return galaxies


def expand_1_dim(data, dim, expand_factor):
	""" Expand galaxies along one dimension in place """
	# Sort list according to dimention
	data.sort(key=lambda x: x[dim])

	# Expand
	prev_galaxy_loc = -1
	for i, g in enumerate(data):
		if (gap := (g[dim] - prev_galaxy_loc - 1)) > 0:
			for j in range(i, len(data)):
				data[j][dim] += gap * (expand_factor - 1)
		prev_galaxy_loc = data[i][dim]
	return None


def distance(g1, g2):
	return sum(abs(g1[i] - g2[i]) for i in range(2))


def do_expand(data, expand_factor):
	data1 = copy.deepcopy(data)
	expand_1_dim(data1, 0, expand_factor)
	expand_1_dim(data1, 1, expand_factor)
	data1.sort()
	return data1


def part1(data, expand_factor):
	"""Solve part 1"""
	galaxies_exp = do_expand(data, expand_factor)
	sum_paths = 0
	for g1, g2 in combinations(galaxies_exp, 2):
		sum_paths += distance(g1, g2)

	return sum_paths


def part2(data):
	"""Solve part 2"""


def solve(puzzle_input):
	"""Solve the puzzle for the given input"""
	data = parse(puzzle_input)
	solution1 = part1(data, EXPAND_FACTOR1)
	solution2 = part1(data, EXPAND_FACTOR2)

	return solution1, solution2


if __name__ == "__main__":
	for path in sys.argv[1:]:
		print(f"{path}:")
		puzzle_input = pathlib.Path(path).read_text().strip()
		solutions = solve(puzzle_input)
		print("\n".join(str(solution) for solution in solutions))
