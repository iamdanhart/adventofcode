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
