from icecream import ic
import re
from collections import defaultdict

class Tile():
    def __init__(self, height):
        self.height = int(height)
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        # self.location = None
        self.trails = []

    def get_trails(self):
        if self.height == 9:
            return [self]
        trails_found = []
        for neigbour in [
            self.top,
            self.bottom,
            self.right,
            self.left
        ]:
            if neigbour and neigbour.height == self.height + 1:
                 trails_found += neigbour.get_trails()
        return trails_found

    def __str__(self):
        # return self.height
        return f'height:{self.height}, trails:{list(map(str, self.trails))}'

if __name__ == '__main__':
    # input_file = '2024/day10/input_example.txt'
    input_file = '2024/day10/input.txt'
    with open(input_file) as f:
        puzzle_input = [list(x) for x in f.read().split('\n')]
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    # ic(puzzle_input)

    min_x, min_y = (0,0)
    max_x, max_y = (len(puzzle_input[0]) - 1, len(puzzle_input) - 1)

    tiles = [list(map(Tile, x)) for x in puzzle_input]
    # ic([list(map(str, x)) for x in tiles])
    # exit()
    # tiles = []
    for y in range(len(tiles)):
        for x in range(len(tiles[y])):
            tile = tiles[y][x]
            # tile.location = (x,y)
            if x > min_x:
                tile.left = tiles[y][x - 1]
                tiles[y][x - 1].right = tile
            if y > min_y:
                tile.top = tiles[y - 1][x]
                tiles[y - 1][x].bottom = tile
            # ic(str(tile))
    score = 0
    for tile in sum(tiles, []):
        if tile.height == 0:
            tile.trails = tile.get_trails()
            # score += len(set(tile.trails))
            score += len(tile.trails)
    ic(score)
    # ic([list(map(str, tile)) for tile in tiles])
    # ic(set(tiles[0][0].get_trails()))
