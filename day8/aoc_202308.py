import pathlib
import sys
import numpy as np

USE_FAST = True


def parse(puzzle_input) -> tuple:
	"""Parse input"""
	lines = puzzle_input.split('\n')
	instruction = lines[0]

	gdata = {}
	for line in lines[2:]:
		source, dests = line.split("=")
		dest1, dest2 = dests.replace("(", "").replace(")", "").split(",")
		gdata[source.replace(" ", "")] = [dest1.replace(" ", ""), dest2.replace(" ", "")]

	return instruction, gdata


def progress_one_step(start: str, step: str, gdata) -> str:
	""" Move one step """
	if step == 'L':
		return gdata[start][0]
	else:
		return gdata[start][1]


def progress_instruction(start: str, instruct: str, gdata):
	res = start
	for s in instruct:
		res = progress_one_step(res, s, gdata)
	return res


def full_instruction_map(instruction, gdata) -> dict:
	full_map = {}
	for start in gdata.keys():
		full_map[start] = progress_instruction(start, instruction, gdata)

	return full_map


def progress_instruction_fast(start, full_map):
	return full_map[start]


def part1(data):
	"""Solve part 1"""
	instruction, gdata = data
	start = 'AAA'
	end = 'ZZZ'
	if start == end:
		return 0

	counter = len(instruction)
	while (dest := progress_instruction(start, instruction, gdata)) != end:
		counter += len(instruction)
		start = dest

	return counter


def part2(data):
	"""Solve part 2"""
	instruction, gdata = data
	vstart = np.array([[x] for x in gdata.keys() if x[-1] == 'A'])
	vend = np.array([[x] for x in gdata.keys() if x[-1] == 'Z'])
	if set(vstart.ravel()) <= set(vend.ravel()):
		return 0

	counter = 0

	if not USE_FAST:
		vprogress_instruction = np.vectorize(progress_instruction)
	else:
		full_map = full_instruction_map(instruction, gdata)
		vprogress_instruction_fast = np.vectorize(progress_instruction_fast)

	while True:
		if counter % 1_000_000 == 0:
			print(f"counter = {counter}")

		counter += len(instruction)
		if not USE_FAST:
			vdest = vprogress_instruction(vstart, instruction, gdata)
		else:
			vdest = vprogress_instruction_fast(vstart, full_map)

		if set(vdest.ravel()) <= set(vend.ravel()):
			return counter
		else:
			vstart = vdest

	return counter


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
