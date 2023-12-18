import pathlib
import sys
import numpy as np
from tqdm import trange
import heapq

# Global parameters
Right = (0, 1)
Down = (1, 0)
Left = (0, -1)
Up = (-1, 0)


def parse(puzzle_input):
	"""Parse input"""
	lines = puzzle_input.split('\n')
	res = []
	for line in lines:
		res.append(np.array([int(e) for e in [*line.strip()]]))
	res = np.array(res)
	return res


def dis_pathfind(world_map, min_conse, max_conse):
	visited = set()
	worklist = [(0, 0, 0, Right, 1), (0, 0, 0, Down, 1)] # cost, x, y, _dir, _dir_count
#	l_c = -1
	while len(worklist) > 0:
		cost, x, y, _dir, _dir_count = heapq.heappop(worklist)
		if (x, y, _dir, _dir_count) in visited:
			continue
		else:
			visited.add((x, y, _dir, _dir_count))
		new_x = x + _dir[1]
		new_y = y + _dir[0]
		if new_x < 0 or new_y < 0 or new_x >= world_map.shape[1] or new_y >= world_map.shape[0]:
			continue
		new_cost = cost + world_map[new_y, new_x]
		if _dir_count >= min_conse and _dir_count <= max_conse:
			if new_x == world_map.shape[1] - 1 and new_y == world_map.shape[0] - 1:
				return new_cost
		for d in [Right, Down, Left, Up]:
			# no reverse
			if d[0] + _dir[0] == 0 and d[1] + _dir[1] == 0:
				continue
			new_d_count = _dir_count + 1 if d == _dir else 1
			if (d != _dir and _dir_count < min_conse) or new_d_count > max_conse:
				continue
			heapq.heappush(worklist, (new_cost, new_x, new_y, d, new_d_count))


def part1(data):
	"""Solve part 1"""
	return dis_pathfind(data, 1,3)

def part2(data):
    """Solve part 2"""
    return dis_pathfind(data, 4, 10)

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
