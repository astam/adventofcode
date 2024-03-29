import sys
from colorama import Fore, Back, Style

# class SubPosition(Position):
#     pass





class Position():
    def __init__(self, character, x, y) -> None:
        self.character = character
        self.x = x
        self.y = y
        self.distance = -1
        self.build_subgrid()
        
    def build_subgrid(self):
        match self.character:
            case '.': subgrid_string = [['.........']]
            case 'S': subgrid_string = [['....S....']]
            case '|': subgrid_string = [['.|..|..|.']]
            case '-': subgrid_string = [['...___...']]
            case 'L': subgrid_string = [['.|..L_...']]
            case 'J': subgrid_string = [['.|._J....']]
            case '7': subgrid_string = [['..._7..|.']]
            case 'F': subgrid_string = [['....F_.|.']]
        self.subgrid = 

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
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid[x])-1):
            print(grid[x][y], end='')
        print()

if __name__ == '__main__':
    input_file = '2023/day10/input_example.txt'
    # input_file = '2023/day10/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))

    sys.setrecursionlimit(20000)
    
    lines.insert(0, '.' * len(lines[0]))
    lines.append('.' * len(lines[0]))
    lines = ['.{}.'.format(x) for x in lines]
    grid = [[y for y in x] for x in lines]
    # print('\n'.join([''.join(x) for x in grid]))

    for x in range(len(lines)):
        # grid.append([])
        for y in range(len(lines[x])):   
            grid[x][y] = Position.get_position(grid[x][y], x, y)

    height = len(lines)
    width = len(lines[0])
    # print('\n'.join([''.join(x) for x in grid]))
    print_grid(grid)
    exit()

    # for x in range(len(grid)):
    #     for y in range(len(grid[x])):
    #         print(grid[x][y], end='')
    #     print('')

    for x in range(1,len(grid)-1):
        for y in range(1,len(grid[x])-1):
            north = grid[x - 1][y]
            south = grid[x + 1][y]
            west = grid[x][y - 1]
            east = grid[x][y + 1]
            grid[x][y].set_neighbours(north, south, east, west)
            # print(grid[x][y], end='')
            if grid[x][y].character == 'S':
                start = grid[x][y]
        # print()
    start.follow()
    # print_grid(grid)
    # exit()

    for x in range(1, height - 1):
        outside = True
        y = 1
        while grid[x][y].character in ' .' and y < width - 1:
            # print_grid(grid)
            # print()
            grid[x][y].character = ' '
            y += 1

    for x in range(1, height - 1):
        outside = True
        y = width - 1
        while grid[x][y].character in ' .' and y > 0:
            # print_grid(grid)
            # print()
            grid[x][y].character = ' '
            y -= 1

    for y in range(1, width - 1):
        outside = True
        x = 1
        while grid[x][y].character in ' .' and x < height - 1:
            # print_grid(grid)
            # print()
            grid[x][y].character = ' '
            x += 1
    
    for y in range(1, width - 1):
        outside = True
        x = height - 1
        while grid[x][y].character in ' .' and x > 0:
            # print_grid(grid)
            # print()
            grid[x][y].character = ' '
            x -= 1
    print_grid(grid)

    count = 0
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            if grid[x][y].character == '.':
                count += 1
    print(count)