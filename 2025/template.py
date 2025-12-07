import pathlib
import time

from util.aoc_utils import read_day_input_as_lines

day = 5

script_dir = pathlib.Path(__file__).parent


def part1(puzzle_input: list[str]) -> int:
    return 0


def part2(puzzle_input: list[str]) -> int:
    return 0


def main():
    test_input = read_day_input_as_lines(__file__, "testinput.txt")
    puzzle_input = read_day_input_as_lines(__file__, "input.txt")

    expected_part1_test_sol = None
    expected_part1_sol = None
    expected_part2_test_sol = None
    expected_part2_sol = None

    sol = part1(test_input)
    if expected_part1_test_sol and sol == expected_part1_test_sol:
        print(f"day {day} part 1test input still correct solution")
    elif expected_part1_test_sol:
        print(f"you broke day {day} part1 test input")

    part1_start = time.time()
    sol = part1(puzzle_input)
    part1_end = time.time()
    if expected_part1_sol and sol == expected_part1_sol:
        print(f"day {day} part 1 input still correct solution")
    elif expected_part1_sol:
        print(f"you broke day {day} part 1 input")
    else:
        print(f"day {day} part 1 input solution: {sol}, solution runtime: {part1_end - part1_start: .4f} seconds")

    sol = part2(test_input)
    if expected_part2_test_sol and sol == expected_part2_test_sol:
        print(f"day {day} part 2 test input still correct solution")
    elif expected_part2_test_sol:
        print(f"you broke day {day} part 2 test input")

    part2_start = time.time()
    sol = part2(puzzle_input)
    part2_end = time.time()
    if expected_part2_sol and sol == expected_part2_sol:
        print(f"day {day} part 2 input still correct solution")
    elif expected_part2_sol:
        print(f"you broke day {day} part 2 input")
    else:
        print(f"day {day} part 2 input solution: {sol}, solution runtime: {part2_end - part2_start: .4f} seconds")


if __name__ == '__main__':
    main()