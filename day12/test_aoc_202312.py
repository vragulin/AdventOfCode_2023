import pathlib

import aoc_202312 as aoc
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
	assert len(example1) == 6
	assert example1[0] == (list('???.###'), [1, 1, 3])


def test_calc_stats_1():
	row = "#.#.###"
	expected = [1, 1, 3]
	actual = aoc.calc_stats(list(row))
	assert expected == actual


def test_calc_stats_2():
	row = ".#.###.#.######"
	expected = [1, 3, 1, 6]
	actual = aoc.calc_stats(list(row))
	assert expected == actual


def test_check_solution_1():
	puzzle = '???.###'
	answer = '#.#'
	stats = [1, 1, 3]
	actual = aoc.check_solution(list(puzzle), stats, answer)
	expected = True
	assert expected == actual


def test_check_solution_false():
	puzzle = '???.###'
	answer = '#..'
	stats = [1, 1, 3]
	actual = aoc.check_solution(list(puzzle), stats, answer)
	expected = False
	assert expected == actual


def test_check_num_solution():
	puzzle = '???.###'
	stats = [1, 1, 3]
	actual = aoc.num_solutions(list(puzzle), stats)
	expected = 1
	assert expected == actual


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
	"""Test part 1 on example input"""
	assert aoc.part1(example1) == 21


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
	"""Test part 2 on example input"""
	assert aoc.part2(example1) == 525152


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
	"""Test part 2 on example input"""
	assert aoc.part2(example2) == ...
