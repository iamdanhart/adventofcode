import time

def read_input(filename):
    with open(filename, 'r') as f:
        return [x.rstrip('\n') for x in f.readlines()]

def split_into_substrings(input: str, length: int) -> list[str]:
    substrings = []
    for i in range(0, len(input), length):
        substrings.append(input[i:i + length])

    return substrings

def contains_cycle_repeated_at_least_twice(val: int) -> bool:
    val_str = str(val)
    num_digits = len(val_str)

    for i in range(1, num_digits // 2 + 1):
        # print(f"cycle len: {i}")
        # substrings = set([''.join(x) for x in itertools.combinations(val_str, i) if ''.join(x) == val_str[0:i]])
        # print(substrings)
        # for substr in substrings:
        #     if len(substr) == num_digits:
        #         return False
        #     if substr * (num_digits // i) == val_str:
        #         # print(f"{val} does contain a cycle {substr}")
        #         return True
        substrings = split_into_substrings(val_str, i)
        if len(set(substrings)) != 1:
            continue
        if len(substrings) > 1:
            # print(f"{val} does contain a cycle")
            return True

    # print(f"{val} does not contain a cycle")
    return False


def contains_cycle_repeated_twice(val: int) -> bool:
    val_str = str(val)
    num_digits = len(val_str)

    substrings = split_into_substrings(val_str, num_digits//2)
    if (len(substrings) == 2) and (substrings[0] == substrings[1]):
        return True
    return False

def cycle_vals_in_range(values: list[int], cycle_check_func = contains_cycle_repeated_twice) -> list[int]:
    cycle_vals = []

    for val in values:
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
    return sum(all_vals_with_cycles)


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
    return sum(all_vals_with_cycles)


def main():
    test_input = read_input("testinput.txt")
    puzzle_input = read_input("input.txt")

    print("day 1, test input")
    sol = day1(test_input)
    if sol == 1227775554:
        print("day 1 test input still correct solution")
    else:
        print("you broke day 1 test input")
    print("day 1, input")
    day1_start = time.time()
    sol = day1(puzzle_input)
    day1_end = time.time()
    if sol == 38158151648:
        print("day 1 input still correct solution")
    else:
        print("you broke day 1 input")
    print(f"day 1 solution runtime: {day1_end - day1_start: .4f} seconds")

    print("day 2, test input")
    sol = day2(test_input)
    if sol == 4174379265:
        print("day 2 test input still correct solution")
    else:
        print("you broke day 2 test input")
        exit()
    print("day 2, input")
    day2_start = time.time()
    sol = day2(puzzle_input)
    day2_end = time.time()
    if sol == 45283684555:
        print("day 2 input still correct solution")
    else:
        print("you broke day 2 input")
    print(f"day 2 solution runtime: {day2_end - day2_start: .4f} seconds")


if __name__ == '__main__':
    main()