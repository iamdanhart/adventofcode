import itertools
import math


def read_input(filename):
    with open(filename, 'r') as f:
        return [x.rstrip('\n') for x in f.readlines()]

def contains_cycle_repeated_at_least_twice(val: int) -> bool:
    val_str = str(val)
    num_digits = len(val_str)

    for i in range(1, num_digits // 2 + 1):
        # print(f"cycle len: {i}")
        substrings = set([''.join(x) for x in itertools.combinations(val_str, i) if ''.join(x) == val_str[0:i]])
        # print(substrings)
        for substr in substrings:
            if len(substr) == num_digits:
                return False
            if substr * (num_digits // i) == val_str:
                # print(f"{val} does contain a cycle {substr}")
                return True

    # print(f"{val} does not contain a cycle")
    return False


def contains_cycle_repeated_twice(val: int) -> bool:
    val_str = str(val)
    num_digits = len(val_str)

    substrings = set([''.join(x) for x in itertools.combinations(val_str, num_digits // 2) if ''.join(x) == val_str[0:num_digits // 2]])
    for substr in substrings:
        if substr * 2 == val_str:
            # print(f"{val} does contain a cycle {substr}")
            return True

    # print(f"{val} does not contain a cycle")
    return False

def cycle_vals_in_range(values: list[int], cycle_check_func = contains_cycle_repeated_twice) -> list[int]:
    cycle_vals = []

    for val in values:
        # if we've found a cycle previously and have a match, skip checking on a certain false
        val_str = str(val)
        half_len = len(val_str) // 2
        # if val_str[:half_len] in [str(x)[:half_len] for x in cycle_vals]:
        #     continue
        if cycle_check_func(val):
            cycle_vals.append(val)

    return cycle_vals

def day1(puzzle_input: list[str]):
    ranges = puzzle_input[0].split(',')

    all_vals_with_cycles = []
    for id_range in ranges:
        id_min, id_max = id_range.split('-')
        range_vals = \
            [x for x in range(int(id_min), int(id_max) + 1) if len(str(x)) % 2 == 0]
        vals_with_cycles = cycle_vals_in_range(range_vals)
        all_vals_with_cycles.extend(vals_with_cycles)
    print(sum(all_vals_with_cycles))


def day2(puzzle_input: list[str]):
    ranges = puzzle_input[0].split(',')

    all_vals_with_cycles = []
    for id_range in ranges:
        id_min, id_max = id_range.split('-')
        range_vals = \
            [x for x in range(int(id_min), int(id_max) + 1)]
        vals_with_cycles = \
            cycle_vals_in_range(range_vals, contains_cycle_repeated_at_least_twice)
        # print(vals_with_cycles)
        all_vals_with_cycles.extend(vals_with_cycles)
        # break
    print(sum(all_vals_with_cycles))


def main():
    test_input = read_input("testinput.txt")
    puzzle_input = read_input("input.txt")

    # print("day 1, test input")
    # day1(test_input)
    # print("day 1, input")
    # day1(puzzle_input)

    # contains_cycle_repeated_at_least_twice(111)
    # print("day 2, test input")
    # day2(test_input)
    print("day 2, input")
    day2(puzzle_input)


if __name__ == '__main__':
    main()