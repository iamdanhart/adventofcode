import pathlib
import time

from util.aoc_utils import read_day_input_as_lines
from util.grid2d import Grid2D

day = 4

script_dir = pathlib.Path(__file__).parent

class ChristmasPaperGrid(Grid2D):
    def count_rolls(self) -> int:
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    continue
                adj = self.adjacent_rolls(i, j)
                if adj < 4:
                    count += 1

        return count

    def adjacent_rolls(self, row, col) -> int:
        if row < 0 or col < 0:
            return 0

        count = 0

        # check above and/or left
        if col > 0 and row > 0:
            count += self.grid[row-1][col-1]
        if row > 0:
            count += self.grid[row-1][col]
        if row > 0 and col < self.width - 1:
            count += self.grid[row-1][col+1]
        if col > 0:
            count += self.grid[row][col-1]

        # check below and/or right
        if col < self.width - 1:
            count += self.grid[row][col+1]
        if col > 0 and row < self.height - 1:
            count += self.grid[row+1][col-1]
        if row < self.height-1:
            count += self.grid[row+1][col]
        if row < self.height - 1 and col < self.width - 1:
            count += self.grid[row+1][col+1]

        return count


    def count_removable(self) -> int:
        removable = 0

        while True:
            removed = 0
            for i in range(self.height):
                for j in range(self.width):
                    if self.grid[i][j] == 0:
                        continue
                    if self.adjacent_rolls(i, j) < 4:
                        removed += 1
                        removable += 1
                        self.update(i, j, 0)

            if removed == 0:
                break

        return removable


def part1(puzzle_input: list[str]):
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    grid = ChristmasPaperGrid(width,height)
    grid.parse_input(puzzle_input, '@', 1)
    return grid.count_rolls()


def part2(puzzle_input: list[str]):
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    grid = ChristmasPaperGrid(width, height)
    grid.parse_input(puzzle_input, '@', 1)
    return grid.count_removable()


def main():
    test_input = read_day_input_as_lines(__file__, "testinput.txt")
    puzzle_input = read_day_input_as_lines(__file__, "input.txt")

    # print(f"day {day} part 1, test input")
    sol = part1(test_input)
    print(sol)
    if sol == 13:
        print(f"day {day} test input still correct solution")
    else:
        print(f"you broke day {day} test input")

    print(f"day {day} part 1, input")
    part1_start = time.time()
    sol = part1(puzzle_input)
    part1_end = time.time()
    if sol == 1537:
        print(f"day {day} input still correct solution")
    else:
        print(f"you broke day {day} input")
    print(f"day {day} solution runtime: {part1_end - part1_start: .4f} seconds")

    print(f"day {day} part 2, test input")
    sol = part2(test_input)
    if sol == 43:
        print(f"day {day} test input still correct solution")
    else:
        print(f"you broke day {day} test input")
        exit()

    print(f"day {day} part 2, input")
    part2_start = time.time()
    sol = part2(puzzle_input)
    part2_end = time.time()
    if sol == 8707:
        print(f"day {day} input still correct solution")
    else:
        print(f"you broke day {day} input")
    print(f"day {day} solution runtime: {part2_end - part2_start: .4f} seconds")


if __name__ == '__main__':
    main()