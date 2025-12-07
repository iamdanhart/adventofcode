import pathlib

def split_into_substrings(input: str, length: int) -> list[str]:
    substrings: list[str] = []
    for i in range(0, len(input), length):
        substrings.append(input[i:i + length])

    return substrings


def read_day_input_as_lines(script_file: str, filename: str = 'input.txt') -> list[str]:
    script_dir = pathlib.Path(script_file).parent

    input_path = script_dir / filename

    with open(input_path, 'r', encoding='utf-8') as f:
        return [x.rstrip('\n') for x in f.readlines()]