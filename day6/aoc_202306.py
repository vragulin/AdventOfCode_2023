import pathlib
import sys
import math


def parse(puzzle_input) -> dict:
	"""Parse input"""
	lines = puzzle_input.split("\n")
	times = [int(x) for x in lines[0].split()[1:]]
	distances = [int(x) for x in lines[1].split()[1:]]
	assert len(times) == len(distances), "Different lengths of times and distances"

	return {'time': times, 'distance': distances}


def num_solutions(time, dist):
	""" Calc number of integer solutions """
	determ = time ** 2 - 4 * dist
	if determ <= 0:
		return 0
	else:
		roots = [(time - math.sqrt(determ)) / 2, (time + math.sqrt(determ)) / 2]
		is_int = (int(roots[0]) * (time - int(roots[0])) == dist)  # Check if the roots are integers
		if is_int:
			return max(roots[1] - roots[0] - 1, 0)
		else:
			return math.floor(roots[1]) - math.ceil(roots[0]) + 1


def part1(data) -> float:
	"""Solve part 1"""
	prod = 1
	for time, dist in zip(data['time'], data['distance']):
		n_solutions = num_solutions(time, dist)
		prod *= n_solutions
		if n_solutions == 0:
			print(f"No solutions for t={time}, d={dist}")
			break
	return prod


def part2(data):
	"""Solve part 2"""
	# Merge inputs
	time, dist = "", ""
	for t, d in zip(data['time'], data['distance']):
		time += str(t)
		dist += str(d)

	return num_solutions(int(time), int(dist))


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
