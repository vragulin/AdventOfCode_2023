import pathlib
import numpy as np
import aoc_202316 as aoc
from aoc_202316 import BEAMS, ENERGY
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
	assert example1.shape == (10, 10)
	assert (example1[0, :] == np.array(list(r'.|...\....'))).all()
	assert (example1[-1, :] == np.array(list(r'..//.|....'))).all()


def test_print_matrix(example1):
	mpaths = np.zeros(example1.shape)
	mpaths[0, :2] = np.array(list([3, 3]))
	aoc.print_matrix(example1, mpaths)
	aoc.print_matrix(example1, mpaths, rpt_type=ENERGY)
	assert True


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 46


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
	"""Test part 2 on example input"""
	assert aoc.part2(example1) == 51


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == ...
