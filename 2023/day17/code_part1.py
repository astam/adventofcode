from __future__ import annotations
from dataclasses import dataclass
import pysnooper
import sys

class CityBlock():
    def __init__(self, heatloss) -> None:
        self.heatloss = heatloss
        self.neighbours = {}
        self.x = -1
        self.y = -1
        self.inpath = False
        self.cache = {}
        self.opposites = {
            'left': 'right',
            'right': 'left',
            'up': 'down',
            'down': 'up'
        }
        # self.path = []
        # self.right = None
        # self.left = None
        # self.top = None
        # self.bottom = None

    def __str__(self) -> str:
        return self.heatloss
    
    def print(self):
        print(self.x, self.y, self.heatloss, self.cache)

    def follow(self, direction=None, straight_steps=0):
        self.print()
        # print(direction)
        # print(self.cache)
        self.inpath = True
        if 'right' not in self.neighbours and 'down' not in self.neighbours:
            return int(self.heatloss)
        for key in self.neighbours:
            if key not in self.cache:
                self.cache[key] = -1
        for key, neighbour in self.neighbours.items():
            if self.cache[key] == -1:
                if not direction or direction != self.opposites[key]:
                    if not (straight_steps == 3 and key == direction):
                        if key == direction:
                            straight_steps += 1
                        else:
                            straight_steps = 0
                        
                        # print(self.cache)
                        # self.cache[key] = -1
                        self.cache[key] = neighbour.follow(direction=key, straight_steps=straight_steps)
        self.print()
        return int(self.heatloss) + min(x for x in self.cache.values())

        

    # def follow_old(self, direction='', straight_steps=0):
        
    #     self.inpath = True
    #     # print(path)
    #     print(self.x, self.y, direction, straight_steps)
    #     # straight_steps += 1
    #     if direction == '':
    #         for key, neighbour in self.neighbours.items():
    #             # print(neighbour, key)
    #             # path.append(neighbour)
    #             self.cache[key] = neighbour.follow(direction=key)


    #     if 'right' not in self.neighbours and 'down' not in self.neighbours:
    #         return (self.heatloss)
    #     for key, neighbour in self.neighbours.items():
    #         if not self.cache[key]:
    #             if opposites[direction] != key:
    #                 if key != direction:
    #                     # path.append(neighbour)
    #                     self.cache[key] = neighbour.follow(direction=key)
    #                 else:
    #                     if straight_steps < 3:
    #                         self.cache[key] = neighbour.follow(direction=key, straight_steps=straight_steps + 1)
        
        

@dataclass
class City():
    grid: list[list:[CityBlock]]

    def __post_init__(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                self.grid[x][y].x = x
                self.grid[x][y].y = y
                if 0 < x:
                    self.grid[x][y].neighbours['up'] = self.grid[x - 1][y]
                if x < len(self.grid) - 1:
                    self.grid[x][y].neighbours['down'] = self.grid[x + 1][y]
                if 0 < y:
                    self.grid[x][y].neighbours['left'] = self.grid[x][y - 1]
                if y < len(self.grid[x]) - 1:
                    self.grid[x][y].neighbours['right'] = self.grid[x][y + 1]

    def __str__(self) -> str:
        result = ''
        for x in self.grid:
            for y in x:
                if y.inpath:
                    result += '*'
                else:
                    result += str(y)
            result += '\n'
        return result

if __name__ == '__main__':
    input_file = '2023/day17/input_example2.txt'
    # input_file = '2023/day17/input.txt'
    input = open(input_file).read().split('\n')
    
    # sys.setrecursionlimit(20000)
    city = City([list(map(CityBlock, x)) for x in input])
    print(city)
    print(city.grid[0][0].follow())
    print(city)