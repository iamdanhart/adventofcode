import time

day = 4

class Grid2D:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for x in range(width)] for y in range(height)]

    def __str__(self) -> str:
        representation = ''
        for y in range(self.height):
            representation += ''.join([str(x) for x in self.grid[y]]) + "\n"
        return representation

    def update(self, row, col, val) -> None:
        self.grid[row][col] = val

    def parse_input(self, input_2d, marker, val):
        for i, row in enumerate(input_2d):
            for j, col in enumerate(row):
                if col == marker:
                    self.update(i, j, val)

    def count_rolls(self) -> int:
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    continue
                # print(f'counting adjacent roles to {i},{j}')
                adj = self.adjacent_rolls(i, j)
                # print(f"counted {adj} rolls")
                if adj < 4:
                    # print(f"{i},{j} is accessible")
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


def read_input(filename) -> list[str]:
    with open(filename, 'r') as f:
        return [x.rstrip('\n') for x in f.readlines()]


def part1(puzzle_input: list[str]):
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    grid = Grid2D(width,height)
    grid.parse_input(puzzle_input, '@', 1)
    # print(grid.adjacent_rolls(0, 2))
    return grid.count_rolls()


def part2(puzzle_input: list[str]):
    width = len(puzzle_input[0])
    height = len(puzzle_input)
    grid = Grid2D(width, height)
    grid.parse_input(puzzle_input, '@', 1)
    return grid.count_removable()


def main():
    test_input = read_input("testinput.txt")
    puzzle_input = read_input("input.txt")

    # print(f"day {day} part 1, test input")
    sol = part1(test_input)
    if sol == 13:
        print(f"day {day} test input still correct solution")
    else:
        print(f"you broke day {day} test input")

    # print(f"day {day} part 1, input")
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