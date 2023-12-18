import pathlib
import sys
import numpy as np
import functools


def parse(puzzle_input):
	"""Parse input"""
	lines = puzzle_input.split("\n")
	data = []
	for line in lines:
		data.append(list(line.strip()))
	return np.array(data)


def calc_load(data):
	nrows, ncols = data.shape
	load_mat = np.zeros(data.shape)

	for i in range(nrows):
		load_mat[i:] = np.where(data[i:] == 'O', nrows - i, 0)

	return np.sum(load_mat)


# @functools.cache
def roll_north(data):
	# First pass - record number of the closest northwise hash location
	closest_hash = np.zeros(data.shape)  # location of closest hash to the north
	stone_num = np.zeros(data.shape)  # number of stone counting from the closest hash

	nrows, ncols = data.shape

	for i in range(nrows):
		if i == 0:
			closest_hash[i, :] = np.where(data[i, :] == '#', 0, -1)
			stone_num[i, :] = np.where(data[i, :] == 'O', 1, 0)
		else:
			closest_hash[i, :] = np.where(data[i, :] == '#', i, closest_hash[i - 1, :])
			stone_num[i, :] = np.where(data[i, :] == "O", stone_num[i - 1] + 1,
			                           np.where(data[i, :] == "#", 0, stone_num[i - 1, :]))

	# For each stone calculate its weight after it has been moved
	stone_rolled_loc = np.where(data == 'O', closest_hash + stone_num, np.nan)
	load = np.where(data == 'O', nrows - stone_rolled_loc, 0)

	rolled_matrix = data.copy()
	for i in range(nrows):
		stone_in_row = np.sum(stone_rolled_loc == i, axis=0)
		rolled_matrix[i, :] = np.where(((data[i, :] == '.') | (data[i, :] == 'O')) & stone_in_row, 'O', '.')
	rolled_matrix = np.where(data == '#', '#', rolled_matrix)
	return np.sum(load), rolled_matrix


def part1(data):
	"""Solve part 1"""
	load, _ = roll_north(data)
	return load


def part2(data):
	"""Solve part 2"""
	spincycles = 1_000_000_000
	cycles, cache = 1, {}
	for i in range(4):
		load, rolled_matrix = roll_north(data)
		data = np.rot90(rolled_matrix, 3)

	while cycles < spincycles:
		for i in range(4):
			load, rolled_matrix = roll_north(data)
			data = np.rot90(rolled_matrix, 3)

		load = calc_load(data)
		cycles += 1
		print(cycles, load)
		new_mat = tuple(tuple(row) for row in data)
		if new_mat in cache:
			cycle_len = cycles - cache[new_mat]
			cycles += ((spincycles - cycles) // cycle_len) * cycle_len
			cache = {}
		else:
			cache[new_mat] = cycles

	return load


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
