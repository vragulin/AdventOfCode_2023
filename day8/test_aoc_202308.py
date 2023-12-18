import pathlib

import aoc_202308 as aoc
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


@pytest.fixture
def example3():
	puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
	return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
	"""Test that input is parsed properly"""
	assert example1[0] == 'RL'
	assert example1[1]['AAA'] == ['BBB', 'CCC']
	assert example1[1]['ZZZ'] == ['ZZZ', 'ZZZ']


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example2(example2):
	"""Test that input is parsed properly"""
	assert example2[0] == 'LLR'
	assert example2[1]['AAA'] == ['BBB', 'BBB']
	assert example2[1]['ZZZ'] == ['ZZZ', 'ZZZ']


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example3(example3):
	"""Test that input is parsed properly"""
	assert example3[0] == 'LR'
	assert example3[1]['11A'] == ['11B', 'XXX']
	assert example3[1]['XXX'] == ['XXX', 'XXX']


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 2


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example2(example2):
	"""Test part 1 on example input"""
	assert aoc.part1(example2) == 6


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example3(example3):
	"""Test part 2 on example input"""
	assert aoc.part2(example3) == 6


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == ...
