from __future__ import annotations
from dataclasses import dataclass
import pysnooper
import sys

class Location():
    def __init__(self, character, depth=0) -> None:
        self.character = character
        self.depth = depth
        self.beamed = False
        self.right = None
        self.left = None
        self.top = None
        self.bottom = None
        self.patterns = []

    def __str__(self) -> str:
        return self.character

    def beam(self, direction, depth):
        self.beamed = True
        self.depth = depth
        pattern = (direction, self.character)
        # print(pattern)
        # print(self.patterns)
        if pattern in self.patterns:
            return
        self.patterns.append(pattern)
        match pattern:
            case ('right', '.') | ('right', '-'):
                if self.right:
                    self.right.beam('right', depth + 1)
            case ('left', '.') | ('left', '-'):
                if self.left:
                    self.left.beam('left', depth + 1)
            case ('up', '.') | ('up', '|'):
                if self.top:
                    self.top.beam('up', depth + 1)
            case ('down', '.') | ('down', '|'):
                if self.bottom:
                    self.bottom.beam('down', depth + 1)
            case ('right', '|') | ('left', '|'):
                if self.top:
                    self.top.beam('up', depth + 1)
                if self.bottom:
                    self.bottom.beam('down', depth + 1)
            case ('up', '-') | ('down', '-'):
                if self.right:
                    self.right.beam('right', depth + 1)
                if self.left:
                    self.left.beam('left', depth + 1)
            case ('right', '\\') | ('left', '/'):
                if self.bottom:
                    self.bottom.beam('down', depth + 1)
            case ('right', '/') | ('left', '\\'):
                if self.top:
                    self.top.beam('up', depth + 1)
            case ('up', '\\') | ('down', '/'):
                if self.left:
                    self.left.beam('left', depth + 1)
            case ('up', '/') | ('down', '\\'):
                if self.right:
                    self.right.beam('right', depth + 1)

@dataclass
class Contraption():
    grid: list[list:[Location]]

    def __post_init__(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if 0 < x:
                    self.grid[x][y].top = self.grid[x - 1][y]
                if x < len(self.grid) - 1:
                    self.grid[x][y].bottom = self.grid[x + 1][y]
                if 0 < y:
                    self.grid[x][y].left = self.grid[x][y - 1]
                if y < len(self.grid[x]) - 1:
                    self.grid[x][y].right = self.grid[x][y + 1]

    def __str__(self) -> str:
        result = ''
        for x in self.grid:
            for y in x:
                result += str(y)
            result += '\n'
        return result
    
    def count_beamed(self):
        result = 0
        for line in self.grid:
            for pos in line:
                if pos.beamed:
                    result += 1
        return result
    
    def print_beamed(self) -> str:
        result = ''
        for x in self.grid:
            for y in x:
                if y.beamed:
                    result += '*'
                else:
                    result += '.'
            result += '\n'
        return result

if __name__ == '__main__':
    input_file = '2023/day16/input_example.txt'
    input_file = '2023/day16/input.txt'
    input = open(input_file).read().split('\n')
    # print(input)
    count = 0
    sys.setrecursionlimit(20000)
    for x in range(len(input)):
        contraption = Contraption([list(map(Location, x)) for x in input])
        contraption.grid[x][0].beam('right', 0)
        count_beamed = contraption.count_beamed()
        count = count_beamed if count < count_beamed else count
        contraption = Contraption([list(map(Location, x)) for x in input])
        contraption.grid[x][-1].beam('left', 0)
        count_beamed = contraption.count_beamed()
        count = count_beamed if count < count_beamed else count
    for y in range(len(input[0])):
        contraption = Contraption([list(map(Location, x)) for x in input])
        contraption.grid[0][y].beam('down', 0)
        count_beamed = contraption.count_beamed()
        count = count_beamed if count < count_beamed else count
        contraption = Contraption([list(map(Location, x)) for x in input])
        contraption.grid[-1][y].beam('up', 0)
        count_beamed = contraption.count_beamed()
        count = count_beamed if count < count_beamed else count

    print(count)

    # contraption.grid[0][0].beam('right', 0)
    # print(contraption.print_beamed())
    # print(contraption.count_beamed())
