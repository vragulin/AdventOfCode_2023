import pathlib

import aoc_202307 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
	puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
	return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
	puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
	return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
	"""Test that input is parsed properly"""
	assert len(example1) == 5
	assert example1[-1] == ('QQQJA', 483)


def test_hand_rank():
	assert aoc.hand_rank('TTTTT') == aoc.FIVE
	assert aoc.hand_rank('TTTT2') == aoc.FOUR
	assert aoc.hand_rank('TT2T2') == aoc.FULL_HOUSE
	assert aoc.hand_rank('TT1T2') == aoc.THREE
	assert aoc.hand_rank('TTMM2') == aoc.TWO_PAIR
	assert aoc.hand_rank('TT123') == aoc.ONE_PAIR
	assert aoc.hand_rank('12345') == aoc.HIGH_CARD


def test_hand_rank_jokers():
	assert aoc.hand_rank_jokers('TTTJJ') == aoc.FIVE
	assert aoc.hand_rank_jokers('JJ223') == aoc.FOUR
	assert aoc.hand_rank_jokers('J3322') == aoc.FULL_HOUSE
	assert aoc.hand_rank_jokers('TT3T2') == aoc.THREE


def test_hand_sort_key():
	assert aoc.hand_sort_key("TTTTT") == '0eeeee'
	assert aoc.hand_sort_key("23456") == '6mlkji'


def test_hand_sort_key_jokers():
	assert aoc.hand_sort_key_jokers("TTTTJ") == '0eeeez'
	assert aoc.hand_sort_key_jokers("J3456") == '5zlkji'


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 6440


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
	"""Test part 2 on example input"""
	assert aoc.part2(example1) == 5905


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == ...
