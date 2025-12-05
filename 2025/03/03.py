import itertools
import time

day = 3

def read_input(filename) -> list[str]:
    with open(filename, 'r') as f:
        return [x.rstrip('\n') for x in f.readlines()]

def find_max_jolts(joltages: list[str], current_combo: str, starting_pos) -> int:
    if len(current_combo) == 12:
        return int(current_combo)
    else:
        available = joltages[starting_pos:]
        max_val = max[available]
        position_of_max = available.index(max_val)


def part1(puzzle_input: list[str]):
    max_jolts: list[int] = []
    for line in puzzle_input:
        bat_joltages: list[str] = [x for x in line]
        combos = itertools.combinations(bat_joltages, 2)
        max_jolt = max(int(''.join(x)) for x in combos)
        max_jolts.append(max_jolt)
    return sum(max_jolts)


def part2(puzzle_input: list[str]):
    joltage = 0
    for line in puzzle_input:
        vals = [int(x) for x in line]
        max_line_joltage = 0
        for i in range(11, -1, -1): # even if biggest digit always at the end, we'll always have at least 1 digit to choose from
            line_len = len(vals)
            possible_vals = vals[ : line_len - i ]  # line_len is always going to be bigger than i
            max_val = max(possible_vals)
            ind_max = possible_vals.index(max_val)
            vals = vals[ind_max + 1:] # most past this digit since we're
            max_line_joltage = max_line_joltage * 10 + max_val
        joltage += max_line_joltage
    return joltage


def main():
    test_input = read_input("testinput.txt")
    puzzle_input = read_input("input.txt")

    print(f"day {day} part 1, test input")
    sol = part1(test_input)
    if sol == 357:
        print(f"day {day} test input still correct solution")
    else:
        print(f"you broke day {day} test input")

    print(f"day {day} part 1, input")
    part1_start = time.time()
    sol = part1(puzzle_input)
    part1_end = time.time()
    if sol == 17301:
        print(f"day {day} input still correct solution")
    else:
        print(f"you broke day {day} input")
    print(f"day {day} solution runtime: {part1_end - part1_start: .4f} seconds")

    print(f"day {day} part 2, test input")
    sol = part2(test_input)
    if sol == 3121910778619:
        print(f"day {day} test input still correct solution")
    else:
        print(f"you broke day {day} test input")
        exit()

    print(f"day {day} part 2, input")
    part2_start = time.time()
    sol = part2(puzzle_input)
    part2_end = time.time()

    if sol == 172162399742349:
        print(f"day {day} input still correct solution")
    else:
        print(f"you broke day {day} input")
    print(f"day {day} solution runtime: {part2_end - part2_start: .4f} seconds")


if __name__ == '__main__':
    main()