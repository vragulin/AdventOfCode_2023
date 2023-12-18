import pathlib

import aoc_202310 as aoc
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


@pytest.fixture
def example4():
	puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
	return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
	"""Test that input is parsed properly"""
	assert len(example1) == 5
	assert example1[1] == list('7S-7|')


def test_find_init_pos_ex1(example1):
	xy_tuple = aoc.find_init_pos(example1)
	assert xy_tuple == (1, 1)


def test_find_init_move_ex1(example1):
	init_pos = (1, 1)
	xy_tuple = aoc.find_init_move(init_pos, example1)
	assert xy_tuple == aoc.RIGHT


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 4


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example2(example2):
	"""Test part 1 on example input"""
	assert aoc.part1(example2) == 8


def test_calc_start_pipe_ex3(example3):
	data = example3
	passes = aoc.calc_path(data)
	assert aoc.calc_start_pipe(passes, data) == 'F'


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example3(example3):
	"""Test part 1 on example input"""
	assert aoc.part2(example3) == 4


def test_part2_example4(example4):
	"""Test part 1 on example input"""
	assert aoc.part2(example4) == 10


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
	"""Test part 2 on example input"""
	assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == ...
