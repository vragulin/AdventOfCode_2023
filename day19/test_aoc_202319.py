import pathlib

import aoc_202319 as aoc
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
	assert len(example1['inst']) == 11
	assert len(example1['parts']) == 5
	assert example1['inst']['hdj'][0]['action'] == 'A'
	assert example1['parts'][-1]['x'] == 2127
	assert example1['first'] == 'in'


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 19114


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
	"""Test part 2 on example input"""
	assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == ...
