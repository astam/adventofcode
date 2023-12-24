from __future__ import annotations
import timeit
from tqdm import tqdm
from dataclasses import dataclass


@dataclass
class Position:
    character: str
    x: int
    y: int

    def __post_init__(self):
        self.north = None
        self.west = None
        self.south = None
        self.east = None

    def __str__(self) -> str:
        return self.character
    
    def move_north(self):
        if self.north:
            if self.character == 'O':
                if self.north.character == '.':
                    self.character = '.'
                    self.north.character = 'O'
            self.north.move_north()

    def get_line_north(self):
        if not self.north:
            return self.character
        else:
            return self.character + self.north.get_line_north()
    
    def move_west(self):
        if self.west:
            if self.character == 'O':
                if self.west.character == '.':
                    self.character = '.'
                    self.west.character = 'O'
            self.west.move_west()

    def get_line_west(self):
        if not self.west:
            return self.character
        else:
            return self.character + self.west.get_line_west()

    def get_line(self):
        if not self.east:
            return self.character
        else:
            return self.character + self.east.get_line()


@dataclass
class Platform():
    grid: list[list[Position]]

    def __post_init__(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if y < len(self.grid[x]) - 1:
                    self.grid[x][y].east = self.grid[x][y + 1]
                if y > 0:
                    self.grid[x][y].west = self.grid[x][y - 1]
                if x < len(self.grid) - 1:
                    self.grid[x][y].south = self.grid[x + 1][y]
                if x > 0:
                    self.grid[x][y].north = self.grid[x - 1][y]

    def move_north(self):
        for pos in self.grid[-1]:
            line = pos.get_line_north()
            # print(line)
            previous_line = ''
            while previous_line != line:
                previous_line = line
                pos.move_north()
                line = pos.get_line_north()
                # print(line)

    def move_west(self):
        for pos in [x[-1] for x in self.grid]:
            line = pos.get_line_west()
            # print(line)
            previous_line = ''
            while previous_line != line:
                previous_line = line
                pos.move_west()
                line = pos.get_line_west()
                # print(line)

    def __str__(self) -> str:
        result = ''
        for line in self.grid:
            result += line[0].get_line()
            # for pos in line:
                # result += str(pos)
            result += '\n'
        return result

if __name__ == '__main__':
    input_file = '2023/day14/input_example.txt'
    input_file = '2023/day14/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    # print()
    platform = Platform([[Position(lines[x][y], x, y) for y in range(len(lines[x]))] for x in range(len(lines))])
    # print(platform)
    # print()    
    starttime = timeit.default_timer()
    platform.move_north()
    # platform.move_west()
    # output = platform.__str__()
    diff =  timeit.default_timer() - starttime
    print("The time difference is :", diff)
    # print()
    # print(platform)
    # print_patform(rotate_platform(platform))
    exit()
    # starttime = timeit.default_timer()
    # for cycle in tqdm(range(1)):
    #     for rotation in range(4):
    #         for _ in range(len(platform)):
    #             for x in range(len(platform) - 1):
    #                 for y in range(len(platform[0])):
    #                     if platform[x + 1][y] == 'O' and platform[x][y] == '.':
    #                         platform[x][y] = 'O'
    #                         platform[x + 1][y] = '.'
    #         print_patform(platform)
    #         print()
    #         platform = rotate_platfor(platform)
        
                    
    # print("The time difference is :", timeit.default_timer() - starttime)

    weight = len(platform)
    load = 0
    for line in platform:
        load += weight * len([x for x in line if x == 'O'])
        weight -= 1
    print(load)