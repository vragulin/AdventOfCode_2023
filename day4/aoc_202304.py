import pathlib
import sys


def parse(puzzle_input):
	"""Parse input"""
	"""Parse input"""
	win_list = []
	my_list = []
	for line in puzzle_input.split("\n"):
		col_idx, pipe_idx = line.find(":"), line.find('|')
		win_nums_s = line[col_idx + 1:pipe_idx].split()
		my_nums_s = line[pipe_idx + 1:].split()
		win_nums = [int(x) for x in win_nums_s]
		my_nums = [int(x) for x in my_nums_s]
		win_list.append(win_nums)
		my_list.append(my_nums)
	return win_list, my_list


def part1(data):
	"""Solve part 1"""
	win_list, my_list = data
	sum_scores = 0
	for win_nums, my_nums in zip(win_list, my_list):
		my_win_num = set(my_nums) & set(win_nums)
		if (matched := len(my_win_num)) > 0:
			sum_scores += 2 ** (matched - 1)
	return sum_scores


def part2(data):
	"""Solve part 2"""
	win_list, my_list = data
	n = len(win_list)
	n_cards = [1] * n
	for i, win_nums, my_nums in zip(range(n), win_list, my_list):
		my_win_num = set(my_nums) & set(win_nums)
		if (matched := len(my_win_num)) > 0:
			for j in range(matched):
				if i + j + 1 < n:
					n_cards[i + j + 1] += n_cards[i]
				else:
					break
	return sum(n_cards)


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
