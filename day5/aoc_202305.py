import pathlib
import sys
import copy

MAPPINGS = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
            'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

def parse(puzzle_input) -> dict:
	"""Parse input"""

	reading_map = None
	map_list = []
	data_dict = {}
	for line in puzzle_input.split("\n"):
		if line[:5] == "seeds":
			data_dict['seeds'] = list(map(int, (line[7:]).split()))
		else:
			tokens = line.split()
			if reading_map is None:
				if len(tokens) == 0:
					continue
				else:
					reading_map = tokens[0]
			else:
				if len(tokens) == 0:
					data_dict[reading_map] = map_list
					reading_map = None
					map_list = []
				else:
					map_line = list(map(int, line.split()))
					map_list.append(map_line)

	# Reached the end of the file, but no empty line to close reading the map
	if reading_map is not None:
		data_dict[reading_map] = map_list

	return data_dict


def do_map(map_list: list, inp: int) -> int:
	""" Execute one of the maps """
	for map_tuple in map_list:
		dest, source, n = map_tuple
		if 0 <= inp - source < n:
			return dest + inp - source
	return inp


def part1(data) -> int:
	"""Solve part 1"""
	res_list = [data['seeds']]
	for m in MAPPINGS:
		def current_map(x):
			return do_map(data[m], x)

		res = list(map(current_map, res_list[-1]))
		res_list.append(res)

	return min(res_list[-1])


def part2_bad_memory(data):
	"""Solve part 2"""
	# Generate a list of seeds
	seeds_list = []
	for i in range(int(len(data['seeds']) / 2)):
		seeds_list += [data['seeds'][2 * i] + x for x in range(data['seeds'][2 * i + 1])]

	data2 = copy.deepcopy(data)
	print("N of seeds = ", len(seeds_list))
	data2['seeds'] = seeds_list
	return part1(data2)


def part2_new(data) -> int:
	"""Solve part 2"""
	min_res = sum(data['seeds']) * 1e6

	for i in range(int(len(data['seeds']) / 2)):
		print(f"Calc seed pair {i}")
		start_range = data['seeds'][2*i]
		end_range = start_range + data['seeds'][2*i+1]
		for seed in range(start_range, end_range):
			res = seed
			for m in MAPPINGS:
				res = do_map(data[m], res)
			min_res = res if res < min_res else min_res

	return min_res


def part2(data):
	#f = part2_bad_memory
	f = part2_new
	return f(data)


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
