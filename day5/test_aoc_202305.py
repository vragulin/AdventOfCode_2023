import pathlib

import aoc_202305 as aoc
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
	assert example1['seeds'] == [79, 14, 55, 13]
	assert example1['seed-to-soil'][1] == [52, 50, 48]
	assert example1['humidity-to-location'][0] == [60, 56, 37]


def test_do_map():
	maps1 = [(50, 98, 2)]
	assert aoc.do_map(maps1, 98) == 50
	assert aoc.do_map(maps1, 99) == 51
	assert aoc.do_map(maps1, 100) == 100
	assert aoc.do_map(maps1, 1) == 1

	maps2 = [(50, 98, 2), (52, 50, 48)]
	assert aoc.do_map(maps2, 98) == 50
	assert aoc.do_map(maps2, 99) == 51
	assert aoc.do_map(maps2, 100) == 100
	assert aoc.do_map(maps2, 1) == 1
	assert aoc.do_map(maps2, 50) == 52


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 35


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
	"""Test part 2 on example input"""
	assert aoc.part2(example1) == 46


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == 82
