import pathlib

import aoc202001 as aoc
import pytest

# PUZZLE_DIR = pathlib.Path(__file__).parent
PUZZLE_DIR = pathlib.Path(__file__).parent / 'templates'


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
	assert example1 == [1721, 979, 366, 299, 675, 1456]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 514579


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
	"""Test part 2 on example input"""
	assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == ...
