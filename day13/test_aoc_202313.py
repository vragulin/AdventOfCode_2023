import pathlib

import aoc_202313 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
	puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
	return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
	puzzle_input = (PUZZLE_DIR / "input1.txt").read_text().strip()
	return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
	"""Test that input is parsed properly"""
	assert len(example1) == 2
	assert len(example1[0]) == 7
	assert len(example1[0][1]) == 9


def test_check_symmetry1(example1):
	array = example1[0][0]
	sym_list = []
	for sym in range(1,len(array)):
		if aoc.check_symmetry(array, sym):
			sym_list.append(sym)

	assert sym_list == [5, 7]


def test_find_all_row_symmetries(example1):
	sym_list = aoc.find_all_row_symmetries(example1[0])
	assert sym_list == [5]

	sym_list = aoc.find_all_row_symmetries(example1[1])
	assert sym_list == []


def test_find_all_col_symmetries(example1):
	sym_list = aoc.find_all_col_symmetries(example1[0])
	assert sym_list == []

	sym_list = aoc.find_all_col_symmetries(example1[1])
	assert sym_list == [4]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 405


def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 405


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part1(example2) == 29037


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == ...
