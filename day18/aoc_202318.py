import pathlib
import sys

# Global parameters
MOVES = {'R': (0, 1),
         'D': (1, 0),
         'L': (0, -1),
         'U': (-1, 0)}

DIRECTIONS = {'0': 'R',
              '1': 'D',
              '2': 'L',
              '3': 'U'}

def parse(puzzle_input):
	"""Parse input"""
	data = []
	for line in puzzle_input.split("\n"):
		line_data = line.replace("(", "").replace(")", "").split()
		data.append([line_data[0], int(line_data[1]), line_data[2]])
	return data


def move_xy(start: tuple, move: tuple) -> tuple:
	x, y = start
	dx, dy = move
	return x + dx, y + dy


def dig_holes(start: tuple, direction: tuple, ncubes: int) -> list:
	""" Generate a tuple of
	:param start:
	:param direction:
	:param ncubes:
	:return:
	"""
	new_trench = []
	curr = start
	for _ in range(ncubes):
		curr = move_xy(curr, direction)
		new_trench.append(curr)
	return new_trench


def calc_polygon_area(vertices: list) -> float:
	""" Use shoelace formula """
	x, y = zip(*vertices)
	return 0.5 * abs(
		sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(vertices)))
	)


def calc_interior_points(area: float, border: int) -> int:
	return int(area - 0.5 * border + 1)


def parse_part2(data) -> None:
	""" Extract directon and distance from the hexadecimal, replace first 2 fields """
	for i, line in enumerate(data):
		data[i][0] = DIRECTIONS[line[2][-1]]
		data[i][1] = int(line[2][1:-1], 16)
	return data


def part1(data):
	"""Solve part 1"""
	trench = [(0, 0)]
	border = 0
	# Dig trench
	for direction, dist, _ in data:
		print(direction, dist)
		new_holes = dig_holes(trench[-1], MOVES[direction], dist)
		trench.append(new_holes[-1])
		border += dist

	# Count interior
	area = calc_polygon_area(trench)
	interior = calc_interior_points(area, border)
	return interior + border


def part2(data):
	"""Solve part 2"""
	parse_part2(data)
	return part1(data)


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
