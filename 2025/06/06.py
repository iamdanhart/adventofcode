import operator
import pathlib
import time

from functools import reduce

from util.aoc_utils import read_day_input_as_lines
from util.grid2d import Grid2D

day = 6

script_dir = pathlib.Path(__file__).parent

class MathHomeworkGrid:
    def __init__(self, width, height, puzzle_input):
        self.width = width
        self.height = height
        self.grid = Grid2D(width, height)

        for i in range(height):
            row = puzzle_input[i].split()
            for j in range(width):
                self.grid.update(i,j, row[j])



    def __str__(self):
        val = ''
        for i in range(self.height):
            row = self.grid[i]
            val += ' '.join(row) + '\n'
        return val

    def calculate_column_part1(self, col_num):
        col_entries = [row[col_num] for row in self.grid]
        op = operator.mul if col_entries[-1] == '*' else operator.add

        return reduce(op, [int(x) for x in col_entries[:-1]])

    def calculate_column_part2(self, col_num):
        col_entries = [row[col_num] for row in self.grid]
        op = operator.mul if col_entries[-1] == '*' else operator.add

        val_width = len(col_entries[0])
        vals = []
        for i in reversed(range(val_width)):
            digits = [e[i] for e  in col_entries[:-1] if e[i] != '0']
            vals.append(''.join(digits))
        return reduce(op, [int(x) for x in vals])

    def calculate_vert_operations_part2(self):
        total = 0
        for i in range(self.width):
            total += self.calculate_column_part2(i)

        return total


    def calculate_vert_operations_part1(self):
        total = 0

        for i in range(self.width):
            total += self.calculate_column_part1(i)

        return total


def part1(puzzle_input: list[str]) -> int:
    width = len(puzzle_input[0].split())
    height = len(puzzle_input)
    grid = MathHomeworkGrid(width, height, puzzle_input)
    return grid.calculate_vert_operations_part1()


def part2(puzzle_input: list[str]) -> int:
    width = len(puzzle_input[0].split())
    height = len(puzzle_input)

    # for the columnar math to add up, we actually need to match the columns as they appear in the input
    # replce all spaces with zeroes, and then for all 0 rows reinsert spaces
    modified_input = []
    longest_row_len = max([len(x) for x in puzzle_input])
    for row in puzzle_input[:-1]:
        mod_row = ''.join([x if x != ' ' else '0' for x in row])
        if len(mod_row) < longest_row_len:
            mod_row += "0" * (longest_row_len - len(mod_row))
        modified_input.append(mod_row)

    for i in range(longest_row_len):
        col_entries = set([x[i] for x in modified_input])
        if len(set(col_entries)) == 1 and '0' in col_entries:
            for j, row in enumerate(modified_input):
                modified_input[j] = row[:i] + ' ' + row[i+1:]

    # add operator row
    modified_input.append(puzzle_input[-1])

    grid = MathHomeworkGrid(width, height, modified_input)
    return grid.calculate_vert_operations_part2()


def main():
    test_input = read_day_input_as_lines(__file__, "testinput.txt")
    puzzle_input = read_day_input_as_lines(__file__, "input.txt")

    expected_part1_test_sol = 4277556
    expected_part1_sol = 4693159084994
    expected_part2_test_sol = 3263827
    expected_part2_sol = 11643736116335

    sol = part1(test_input)
    if expected_part1_test_sol and sol == expected_part1_test_sol:
        print(f"day {day} part 1 test input still correct solution")
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