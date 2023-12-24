import sys
from colorama import Fore, Back, Style

class Position():
    def __init__(self, character, x, y) -> None:
        self.character = character
        self.x = x
        self.y = y
        self.distance = -1
        self.outside = False

    def set_neighbours(self, north, south, east, west):
        self.north = north
        self.south = south
        self.west = west
        self.east = east

    def __str__(self) -> str:
        # style_begin = Style.BRIGHT if self.distance < -1 else ''
        # style_end = Style.RESET_ALL if self.distance < -1 else ''
        # format_string = "\033[92m{}\033[00m" if self.distance > -1 else "{}"
        # style_begin = "\033[92m" if self.distance < -1 else ''
        # style_end = "\033[00m" if self.distance < -1 else ''
        # print("\033[92m{}\033[00m".format(self.character))
        output_character = self.character
        match self.character:
            case '|': output_character = u'\u2502'
            case '-': output_character = u'\u2500'
            case 'L': output_character = u'\u2514'
            case 'J': output_character = u'\u2518'
            case '7': output_character = u'\u2510'
            case 'F': output_character = u'\u250C' 
        return output_character
    
    def find_outsides(self):
        self.outside = True
        self.character = 'O'
        # print(self.x, self.y)
        for pos in [self.north, self.south, self.east, self.west]:
            # print(pos)
            if pos and not pos.outside and pos.distance == -1:
                pos.find_outsides() 
    
    def str_neighbours(self) -> str:
        output = '\n{}\n{}\n {} \n{}{}{}\n {} \n'.format(
            self.__class__.__name__,
            self.distance,
            self.north,
            self.west,
            self,
            self.east,
            self.south
        )
        return output

    @classmethod
    def get_position(cls, character, x, y):
        match character:
            case ' ': return Position(character, x, y)
            case '.': return Ground(character, x, y)
            case 'S': return Start(character, x, y)
            case '|': return NorthSouth(character, x, y)
            case '-': return WestEast(character, x, y)
            case 'L': return NorthEast(character, x, y)
            case 'J': return NorthWest(character, x, y)
            case '7': return SouthWest(character, x, y)
            case 'F': return SouthEast(character, x, y)

class Ground(Position):
    def __init__(self, character, x, y) -> None:
        super().__init__(character, x, y)
        
    
class Pipe(Position):
    pass

class Start(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        # print(self.str_neighbours())
        if self.north.character in '|7F' and self.north.distance == -1:
            self.north.follow(self.distance + 1)
        if self.south.character in '|LJ' and self.south.distance == -1:
            self.south.follow(self.distance + 1)
        if self.east.character in '-J7' and self.east.distance == -1:
            self.east.follow(self.distance + 1)
        if self.west.character in '-LF' and self.west.distance == -1:
            self.west.follow(self.distance + 1)

class NorthSouth(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        # print(self.str_neighbours())
        if self.north.character in '|7F' and self.north.distance == -1:
            self.north.follow(self.distance + 1)
        if self.south.character in '|LJ' and self.south.distance == -1:
            self.south.follow(self.distance + 1)

class WestEast(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        # print(self.str_neighbours())
        if self.east.character in '-J7' and self.east.distance == -1:
            self.east.follow(self.distance + 1)
        if self.west.character in '-LF' and self.west.distance == -1:
            self.west.follow(self.distance + 1)

class NorthEast(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        # print(self.str_neighbours())
        if self.north.character in '|7F' and self.north.distance == -1:
            self.north.follow(self.distance + 1)
        if self.east.character in '-J7' and self.east.distance == -1:
            self.east.follow(self.distance + 1)

class NorthWest(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        # print(self.str_neighbours())
        if self.north.character in '|7F' and self.north.distance == -1:
            self.north.follow(self.distance + 1)
        if self.west.character in '-LF' and self.west.distance == -1:
            self.west.follow(self.distance + 1)

class SouthWest(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        # print(self.str_neighbours())
        if self.south.character in '|LJ' and self.south.distance == -1:
            self.south.follow(self.distance + 1)
        if self.west.character in '-LF' and self.west.distance == -1:
            self.west.follow(self.distance + 1)

class SouthEast(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        # print(self.str_neighbours())
        if self.south.character in '|LJ' and self.south.distance == -1:
            self.south.follow(self.distance + 1)
        if self.east.character in '-J7' and self.east.distance == -1:
            self.east.follow(self.distance + 1)

def print_grid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            print(grid[x][y], end='')
        print()

if __name__ == '__main__':
    input_file = '2023/day10/input_example3.txt'
    input_file = '2023/day10/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))

    sys.setrecursionlimit(200000)
    
    lines.insert(0, '.' * len(lines[0]))
    lines.append('.' * len(lines[0]))
    lines = ['.{}.'.format(x) for x in lines]
    grid = [[' ' for y in range(len(lines[0]) * 3)] for x in range(len(lines) * 3)]
    # grid = [[y for y in x] for x in lines]
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            grid[x * 3 + 1][y * 3 + 1] = lines[x][y]
            if lines[x][y] in 'S|LJ':
                grid[x * 3 + 0][y * 3 + 1] = '|'
            if lines[x][y] in 'S|7F':
                grid[x * 3 + 2][y * 3 + 1] = '|'
            if lines[x][y] in 'S-7J':
                grid[x * 3 + 1][y * 3 + 0] = '-'
            if lines[x][y] in 'S-LF':
                grid[x * 3 + 1][y * 3 + 2] = '-'

    # print('\n'.join([''.join(x) for x in grid])) 
    # exit()

    for x in range(len(grid)):
        # grid.append([])
        for y in range(len(grid[x])):   
            grid[x][y] = Position.get_position(grid[x][y], x, y)

    height = len(grid)
    width = len(grid[0])
    # print('\n'.join([''.join(x) for x in grid]))
    # print_grid(grid)
    # exit()

    # for x in range(len(grid)):
    #     for y in range(len(grid[x])):
    #         print(grid[x][y], end='')
    #     print('')

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            north, south, west, east = None, None, None, None
            if 1 <= x < len(grid):
                north = grid[x - 1][y]
            if 1 <= y < len(grid[x]):
                west = grid[x][y - 1]
            if 0 <= x < len(grid) - 1:
                south = grid[x + 1][y]
            if 0 <= y < len(grid[x]) - 1:
                east = grid[x][y + 1]
            grid[x][y].set_neighbours(north, south, east, west)
            # print(grid[x][y], end='')
            if grid[x][y].character == 'S':
                start = grid[x][y]
        # print()
    start.follow()
    grid[0][0].find_outsides()
    print_grid(grid)

    count = 0
    for x in range(1, height + 1, 3):
        for y in range(1, width + 1, 3):
            if not grid[x][y].outside and grid[x][y].distance == -1:
                count += 1
    print(count)