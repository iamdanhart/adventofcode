import pathlib
import time

from util.aoc_utils import read_day_input_as_lines

day = 5

script_dir = pathlib.Path(__file__).parent

def read_input(puzzle_input: list[str]) -> tuple[list[str], list[str]]:
    ranges: list[str] = []
    ids: list[str] = []

    reading_ranges = True
    for line in puzzle_input:
        if line.strip() == "":
            reading_ranges = False
            continue

        if reading_ranges:
            ranges.append(line)
        else:
            ids.append(line)

    return ranges, ids

def count_fresh(ranges: list[str], ids: list[str]) -> int:
    fresh_count = 0

    for val in ids:
        id = int(val)
        for r in ranges:
            low, high = [int(x) for x in r.split("-")]
            if low <= id <= high:
                # print(f"{val} is fresh in {low}-{high}")
                fresh_count += 1
                break # don't double count an id if it's good for multiple ranges


    return fresh_count


def part1(puzzle_input: list[str]) -> int:
    ranges, ids = read_input(puzzle_input)
    return count_fresh(ranges, ids)


def part2(puzzle_input: list[str]) -> int:
    """
    This assumes the ranges are sorted in order by low range

    Scenarios:

        for no overlap, the next row's low must exceed the previous row's high
        [1, 2]
        [3, 4]
        count range of both

        for overlap to occur, the following must be true:
        the next row's low must bw equal to the previous row's low
        the next row's low must be less than or equal to the previous row's high
        combine the ranges in order to not double-count overlap

        [1, 2]
        [2, 2]
        should result in [1,2]

        [1, 2]
        [1, 9]
        should result in [1,9]

        [1, 9]
        [1, 2]
        should result in [1, 9]

        min of the lows (by virtue of sorting, the first low will be equal or less than), max of the highs

    :param puzzle_input:
    :return:
    """
    fresh_id_count = 0

    ranges, _ = read_input(puzzle_input)
    ranges = tuple([[int(x) for x in y.split("-")] for y in ranges])
    ranges = sorted(ranges, key=lambda x: x[0])
    prev_low, prev_high = ranges[0]
    ranges_unique: list[tuple[int, int]] = []
    for curr in ranges[1:]:
        curr_low, curr_high = curr

        if curr_low <= prev_high:
            prev_high = max(curr_high, prev_high)
        else:
            ranges_unique.append((prev_low, prev_high))
            prev_low, prev_high = curr_low, curr_high
    ranges_unique.append((prev_low, prev_high))

    for r in ranges_unique:
        fresh_id_count += r[1] - r[0] + 1

    return fresh_id_count


def main():
    test_input = read_day_input_as_lines(__file__, "testinput.txt")
    puzzle_input = read_day_input_as_lines(__file__, "input.txt")

    expected_part1_test_sol = 3
    expected_part1_sol = 567
    expected_part2_test_sol = 14
    expected_part2_sol = None

    sol = part1(test_input)
    if expected_part1_test_sol and sol == expected_part1_test_sol:
        print(f"day {day} part 1 test input still correct solution")
    elif expected_part1_test_sol:
        print(f"you broke day {day} part1 test input, expected {expected_part1_test_sol} got {sol}")

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
        print(f"you broke day {day} part 2 test input, expected {expected_part2_test_sol} got {sol}")

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