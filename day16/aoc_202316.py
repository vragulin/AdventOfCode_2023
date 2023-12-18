import pathlib
import sys
import numpy as np
from collections import deque, namedtuple

# Report types
BEAMS, ENERGY = range(2)
Beam = namedtuple("Beam", "loc dir")

REFLECT = {
	('>', '|'): ('v', '^'),
	('<', '|'): ('v', '^'),
	('>', '/'): ('^',),
	('<', '/'): ('v',),
	('>', '\\'): ('v',),
	('<', '\\'): ('^',),
	('^', '-'): ('>', '<'),
	('v', '-'): ('>', '<'),
	('^', '/'): ('>',),
	('v', '/'): ('<',),
	('^', '\\'): ('<',),
	('v', '\\'): ('>',),
}


def parse(puzzle_input):
	"""Parse input"""
	lines = puzzle_input.split("\n")
	data = []
	for line in lines:
		data.append(list(line.strip()))
	return np.array(data)


def print_matrix(init: np.array, mpaths: np.array, rpt_type: int = BEAMS):
	""" Print matrix showing beam paths """
	nrows, ncols = init.shape

	if rpt_type == ENERGY:
		print_data = np.where(mpaths == 0, '.', "#")
	else:
		print_data = np.where(np.isin(init, list('-|/\\')), init, mpaths.astype(int))

	print("\n")
	for i in range(nrows):
		for j in range(ncols):
			print(f"{print_data[i, j]:<2}", end="")
		print("\n")


def update_mpath(old_value, direction):
	dir_values = {'^': 1, 'v': 2, '>': 3, '<': 4}
	# Check if we have already visited this cell in the same direction
	power_of_2 = 2 ** dir_values[direction]
	remainder = old_value % power_of_2
	if remainder >= power_of_2 / 2:
		return -1  # Have visited
	else:
		return old_value + power_of_2 / 2  # Updated


def one_step(beams: deque, init: np.array, mpaths: np.array) -> int:
	""" Move one beam one step, check if it has left the grid
		Update the stack, return remaining number of beams
	"""
	nrows, ncols = init.shape

	# Pop a bream from the stock
	actv_beam = beams.pop()

	# Update location o fthe actie beam and check if the beam has left the grid
	if actv_beam.dir == ">":
		new_loc = (actv_beam.loc[0], actv_beam.loc[1] + 1)
	elif actv_beam.dir == "<":
		new_loc = (actv_beam.loc[0], actv_beam.loc[1] - 1)
	elif actv_beam.dir == "v":
		new_loc = (actv_beam.loc[0] + 1, actv_beam.loc[1])
	else:
		new_loc = (actv_beam.loc[0] - 1, actv_beam.loc[1])

	if (-1 < new_loc[0] < nrows) and (-1 < new_loc[1] < ncols):  # If the beam has not left the grid

		# Update mpaths array of where beams have travelled
		new_code = update_mpath(mpaths[new_loc], actv_beam.dir)
		if new_code < 0:  # We are in a loop
			return len(beams)
		else:
			mpaths[new_loc] = new_code

		# Check if we change direction and place the updated beam and children on the stack
		refl_dirs = REFLECT.get((actv_beam.dir, init[new_loc]),
		                        (actv_beam.dir,))

		for refl_dir in refl_dirs:
			new_beam = Beam(loc=new_loc, dir=refl_dir)
			if new_beam not in beams:
				beams.append(new_beam)

	return len(beams)


def num_energized(first_beam, data, verbose: bool = False):
	mpaths = np.zeros(data.shape)

	# Initialize the beam
	beams = deque()
	beams.append(first_beam)

	counter = 0
	# cache = {}
	while one_step(beams, data, mpaths) > 0:
		counter += 1
		if counter % 200000 == 0:
			print(f"counter = {counter}")

	# Print results and calc the answer
	if verbose:
		print_matrix(data, mpaths, rpt_type=BEAMS)
		print_matrix(data, mpaths, rpt_type=ENERGY)
	return np.sum(mpaths > 0)


def part1(data):
	"""Solve part 1"""
	# Create a matrix to keep track of the paths
	first_beam = Beam((0, -1), '>')
	return num_energized(first_beam, data, True)


def part2(data):
	"""Solve part 2"""
	# Build an array of trial first beams
	nrows, ncols = data.shape
	first_beams = []
	for i in range(nrows):
		first_beams.append(Beam((i, -1), '>'))
		first_beams.append(Beam((i, ncols), '<'))

	for j in range(ncols):
		first_beams.append(Beam((-1, j), 'v'))
		first_beams.append(Beam((nrows, j), '^'))

	nrg_vals = []
	for first_beam in first_beams:
		nrg_vals.append(num_energized(first_beam, data))

	return max(nrg_vals)


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
