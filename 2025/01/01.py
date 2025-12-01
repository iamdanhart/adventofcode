

dial_positions = [x for x in range(0, 100)]

def read_input(filename):
    with open(filename, 'r') as f:
        return [x.rstrip('\n') for x in f.readlines()]

def move_dial_day1(start_position, direction, distance) -> int:
    if direction == 'L':
        return (start_position - distance) % 100
    else:
        return (start_position + distance) % 100


# return the new position and number of times that 0 was ticked along the way
def move_dial_day2(start_position, direction, distance) -> tuple[int, int]:
    times_ticked = 0
    while distance > 100:
        times_ticked += 1
        distance -= 100
    stop_position = move_dial_day1(start_position, direction, distance)
    if distance < 100 and start_position != 0 and stop_position != 0 and ((direction == 'L' and stop_position > start_position) or (direction == 'R' and stop_position < start_position)):
        times_ticked += 1
    print(
        f"started at {start_position}, moved {direction} {distance}, ended at {stop_position}, passed 0 {times_ticked} times")
    return stop_position, times_ticked


def day1(puzzle_input: list[str]):
    pw = 0
    dial_position = 50
    for dial_movement in puzzle_input:
        direction, distance = dial_movement[0], int(dial_movement[1:])
        prev_position = dial_position
        dial_position = move_dial_day1(dial_position, direction, distance)
        # print(prev_position, distance, direction, dial_position)
        if prev_position != 0 and dial_position == 0:
            pw += 1
    print("pw is", pw)


def day2(puzzle_input: list[str]):
    pw = 0
    dial_position = 50
    for dial_movement in puzzle_input:
        direction, distance = dial_movement[0], int(dial_movement[1:])
        prev_position = dial_position
        dial_position, times_ticked = move_dial_day2(dial_position, direction, distance)
        pw += times_ticked
        if prev_position != 0 and dial_position == 0:
            pw += 1
    print("pw is", pw)


def main():
    test_input = read_input("testinput.txt")
    puzzle_input = read_input("input.txt")

    print("day 1, test input")
    day1(test_input)
    print("day 1, input")
    day1(puzzle_input)

    print("day 2, test input")
    day2(test_input)
    print("day 2, input")
    day2(puzzle_input)


if __name__ == '__main__':
    main()