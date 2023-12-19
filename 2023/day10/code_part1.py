import sys

class Position():
    def __init__(self, character, x, y) -> None:
        self.character = character
        self.x = x
        self.y = y
        self.distance = -1

    def set_neighbours(self, north, south, east, west):
        self.north = north
        self.south = south
        self.west = west
        self.east = east

    def __str__(self) -> str:
        return self.character
    
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
    pass

class Pipe(Position):
    pass

class Start(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        print(self.str_neighbours())
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
        print(self.str_neighbours())
        if self.north.character in '|7F' and self.north.distance == -1:
            self.north.follow(self.distance + 1)
        if self.south.character in '|LJ' and self.south.distance == -1:
            self.south.follow(self.distance + 1)

class WestEast(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        print(self.str_neighbours())
        if self.east.character in '-J7' and self.east.distance == -1:
            self.east.follow(self.distance + 1)
        if self.west.character in '-LF' and self.west.distance == -1:
            self.west.follow(self.distance + 1)

class NorthEast(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        print(self.str_neighbours())
        if self.north.character in '|7F' and self.north.distance == -1:
            self.north.follow(self.distance + 1)
        if self.east.character in '-J7' and self.east.distance == -1:
            self.east.follow(self.distance + 1)

class NorthWest(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        print(self.str_neighbours())
        if self.north.character in '|7F' and self.north.distance == -1:
            self.north.follow(self.distance + 1)
        if self.west.character in '-LF' and self.west.distance == -1:
            self.west.follow(self.distance + 1)

class SouthWest(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        print(self.str_neighbours())
        if self.south.character in '|LJ' and self.south.distance == -1:
            self.south.follow(self.distance + 1)
        if self.west.character in '-LF' and self.west.distance == -1:
            self.west.follow(self.distance + 1)

class SouthEast(Pipe):

    def follow(self, distance=0):
        self.distance = distance
        print(self.str_neighbours())
        if self.south.character in '|LJ' and self.south.distance == -1:
            self.south.follow(self.distance + 1)
        if self.east.character in '-J7' and self.east.distance == -1:
            self.east.follow(self.distance + 1)


if __name__ == '__main__':
    input_file = '2023/day10/input_example2.txt'
    input_file = '2023/day10/input.txt'
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
    # print('\n'.join([''.join(x) for x in grid]))
    # print(grid)

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
            print(grid[x][y], end='')
            if grid[x][y].character == 'S':
                start = grid[x][y]
        print()
    start.follow()