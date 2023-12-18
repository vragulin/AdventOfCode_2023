import pathlib
import sys
import numpy as np

# moves
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# current previous move
# |       DOWN     DOWN
# |       UP       UP
# ...
moves = {
	('|', DOWN): DOWN,
	('|', UP): UP,
	('-', RIGHT): RIGHT,
	('-', LEFT): LEFT,
	('L', LEFT): UP,
	('L', DOWN): RIGHT,
	('J', RIGHT): UP,
	('J', DOWN): LEFT,
	('7', RIGHT): DOWN,
	('7', UP): LEFT,
	('F', LEFT): DOWN,
	('F', UP): RIGHT
}


def get_pipe(xy_tuple, data):
	""" read pipe in a mace position """
	x, y = xy_tuple
	return data[y][x]


def new_pos(pos, dir):
	return tuple(a + b for a, b in zip(pos, dir))


def parse(puzzle_input):
	"""Parse input"""
	lines = puzzle_input.split('\n')
	s_list = []
	for line in lines:
		series = list(line)
		s_list.append(series)
	return s_list


def find_init_pos(data) -> tuple:
	for y, line in enumerate(data):
		if 'S' in line:
			x = line.index('S')
			break
	return x, y


def find_init_move(xy_tuple, data) -> tuple:
	# Try cells in the following order: URDL
	x, y = xy_tuple
	if (y > 0) and get_pipe(new_pos(xy_tuple, UP), data) in ['|', '7', 'F']:
		init_move = UP
	elif (x < len(data[0]) - 1) and get_pipe(new_pos(xy_tuple, RIGHT), data) in ['-', '7', 'J']:
		init_move = RIGHT
	elif (y < len(data) - 1) and get_pipe(new_pos(xy_tuple, DOWN), data) in ['|', 'L', 'J']:
		init_move = DOWN
	elif (x > 0) and get_pipe(new_pos(xy_tuple, LEFT), data) in ['-', 'L', 'F']:
		init_move = LEFT
	else:
		raise ValueError("S is not connected")
	return init_move


def calc_path(data):
	start_pos = find_init_pos(data)
	start_move = find_init_move(start_pos, data)

	pos = start_pos
	dir = start_move

	passes = [start_pos]

	while True:
		pos = new_pos(pos, dir)
		cur = get_pipe(pos, data)
		if pos == start_pos:
			break
		dir = moves[(cur, dir)]
		passes.append(pos)

	return passes


def calc_start_pipe(passes, data) -> str:
	""" Replace S with an appropriate pipe so that we have a full loop
	"""
	last_move = tuple(passes[0][i] - passes[-1][i] for i in range(2))
	first_move = tuple(passes[1][i] - passes[0][i] for i in range(2))

	pipe_dict = {
		(UP, UP): '|',
		(UP, LEFT): '7',
		(UP, RIGHT): 'F',
		(DOWN, DOWN): '|',
		(DOWN, LEFT): 'J',
		(DOWN, RIGHT): 'L',
		(LEFT, UP): 'L',
		(LEFT, DOWN): 'F',
		(LEFT, LEFT): '-',
		(RIGHT, UP): 'J',
		(RIGHT, DOWN): '7',
		(RIGHT, RIGHT): '-',
	}

	return pipe_dict[(last_move, first_move)]


def part1(data):
	"""Solve part 1"""
	passes = calc_path(data)
	return len(passes) // 2


def part2(data):
	"""Solve part 2"""
	passes = calc_path(data)

	# First replace S with the appropirate pipe
	start_pipe = calc_start_pipe(passes, data)
	data[passes[0][1]][passes[0][0]] = start_pipe

	# Mark points not in the pipe
	insiders = []
	for y, line in enumerate(data):
		is_in = False
		if (y == 0) or (y == len(data) - 1):
			continue
		else:
			for x, _ in enumerate(line):
				if (x, y) in passes:
					if data[y][x] in ('|', 'J', 'L'):
						is_in = not is_in
				elif is_in:
					insiders.append((x, y))

	return len(insiders)


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
