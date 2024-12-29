from icecream import ic
import re
from collections import defaultdict

class Area():
    def __init__(self, label:chr):
        self.region = None
        self.label = label
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    def __str__(self):
        return self.label

if __name__ == '__main__':
    input_file = '2024/day12/input_example.txt'
    # input_file = '2024/day12/input.txt'
    with open(input_file) as f:
        puzzle_input = [list(x) for x in f.read().split('\n')]
    ic(puzzle_input)

    areas = [list(map(Area, x)) for x in puzzle_input]
    ic([list(map(str, x)) for x in areas])


    min_x, min_y = (0,0)
    max_x, max_y = (len(areas[0]) - 1, len(areas) - 1)

    for y in range(len(areas)):
        for x in range(len(areas[y])):
            tile = areas[y][x]
            if x > min_x:
                tile.left = areas[y][x - 1]
                areas[y][x - 1].right = tile
            if y > min_y:
                tile.top = areas[y - 1][x]
                areas[y - 1][x].bottom = tile
    
    

