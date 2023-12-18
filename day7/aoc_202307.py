import itertools
import pathlib
import sys
from collections import Counter
from itertools import combinations

FIVE, FOUR, FULL_HOUSE, THREE, TWO_PAIR, ONE_PAIR, HIGH_CARD = range(7)
RANKS = list('AKQJT98765432')


def parse(puzzle_input) -> list:
	"""Parse input"""
	lines = puzzle_input.split("\n")
	game = []
	for line in lines:
		tokens = line.split()
		game.append((tokens[0], int(tokens[1])))
	return game


def hand_rank(hand):
	""" Generate a string that starts with the rank of the hand
		in the first character, followed by the card list.
		This string can be used as the sort key
	"""
	cards = Counter(list(hand))
	combinations = sorted(cards.values(), reverse=True)

	if combinations[0] == 5:
		return FIVE
	elif combinations[0] == 4:
		return FOUR
	elif combinations[0] == 3:
		if combinations[1] == 2:
			return FULL_HOUSE
		else:
			return THREE
	elif combinations[0] == 2:
		if combinations[1] == 2:
			return TWO_PAIR
		else:
			return ONE_PAIR
	else:
		return HIGH_CARD


def hand_rank_jokers(hand):
	""" Use jokers to determine the maximum hand rank """
	cards = Counter(list(hand))
	if cards.get('J', 0) == 0:
		return hand_rank(hand)
	else:
		best_rank = HIGH_CARD
		n_jokers = cards['J']
		for j_combo in itertools.combinations_with_replacement(RANKS, n_jokers):
			new_hand = hand
			for j_use in j_combo:
				new_hand = new_hand.replace('J', j_use, 1)
			if (new_rank := hand_rank(new_hand)) < best_rank:
				best_rank = new_rank
			if best_rank == 0:
				break
		return best_rank


def hand_enconding(hand):
	codes = list('abcdefghijklm')
	code = hand
	for r, c in zip(RANKS, codes):
		code = code.replace(r, c)
	return code


def hand_enconding_jokers(hand):
	ranks = RANKS
	codes = list('abczefghijklm')
	code = hand
	for r, c in zip(ranks, codes):
		code = code.replace(r, c)
	return code


def hand_sort_key(hand):
	return str(hand_rank(hand)) + hand_enconding(hand)


def hand_sort_key_jokers(hand):
	return str(hand_rank_jokers(hand)) + hand_enconding_jokers(hand)


def part1(data) -> int:
	"""Solve part 1"""
	sorted_data = sorted(data, key=lambda x: hand_sort_key(x[0]), reverse=True)
	res = 0
	for i, _ in enumerate(sorted_data):
		res += (i + 1) * sorted_data[i][1]
	return res


def part2(data) -> int:
	"""Solve part 2"""
	sorted_data = sorted(data, key=lambda x: hand_sort_key_jokers(x[0]), reverse=True)
	res = 0
	for i, _ in enumerate(sorted_data):
		res += (i + 1) * sorted_data[i][1]
	return res

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
