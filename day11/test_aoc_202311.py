import pathlib

import aoc_202311 as aoc
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
	assert example1[:2] == [[0, 3], [1, 7]]
	assert example1[-1] == [9, 4]


def test_distance1():
	assert aoc.distance([0, 0], [1, 2]) == 3


def test_expand_1_dim_ex2(example1):
	# test expand
	galaxies = aoc.do_expand(example1, 2)
	galaxies.sort()
	assert galaxies[:2] == [[0, 4], [1, 9]]
	assert galaxies[-1] == [11, 5]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1_ex2(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1, 2) == 374


def test_part1_example1_ex10(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1, 10) == 1030


def test_part1_example1_ex100(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1, 100) == 8410

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
	"""Test part 2 on example input"""
	assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == ...
