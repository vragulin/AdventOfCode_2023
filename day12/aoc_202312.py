import pathlib
import sys
import itertools


def parse(puzzle_input: list):
	"""Parse input"""
	lines = lines = puzzle_input.split('\n')
	data = []
	for line in lines:
		puzzle, rest = line.split(" ")
		groups_str = rest.split(",")
		groups = [int(x) for x in groups_str]
		data.append((list(puzzle), groups))

	return data


def calc_stats(row: list):
	broken = []
	n_broken = 0

	for c in row:
		if c == '#':
			n_broken += 1
		elif n_broken > 0:
			broken.append(n_broken)
			n_broken = 0

	if n_broken > 0:
		broken.append(n_broken)
	return broken


def check_solution(puzzle: list, stats: list, answer: str) -> bool:
	# Replace ? with the answer
	p_list = list(puzzle)
	cur_q = 0
	for i, c in enumerate(puzzle):
		if c == '?':
			p_list[i] = answer[cur_q]
			cur_q += 1

	# Check if the solution matches the answer
	return calc_stats(p_list) == stats


def num_solutions(puzzle: list, stats: list) -> int:
	n_quest = sum([x == '?' for x in puzzle])
	counter = 0
	for guess in list(itertools.product(*([['.', '#']] * n_quest))):
		counter += check_solution(puzzle, stats, guess)
	return counter


def part1(data):
	"""Solve part 1"""
	sum_all = 0
	for puzzle, stats in data:
		sum_all += num_solutions(puzzle, stats)
	return sum_all


def part2(data):
	"""Solve part 2"""
	"""Solve part 1"""
	sum_all = 0
	for puzzle, stats in data:
		puzzle1 = puzzle * 5
		stats1 = stats * 5
		sum_all += num_solutions(puzzle1, stats1)
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
