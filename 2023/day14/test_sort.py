from __future__ import annotations
import timeit
from tqdm import tqdm
from dataclasses import dataclass
from functools import lru_cache

@dataclass
class Char():
    character: chr
    east: Char = None

    def get_line(self):
        if not self.east:
            return self.character
        else:
            return self.character + self.east.get_line()
        
    def move_east(self, line=[], rocks=0, empties=0):
        if line == []:
            return '.' * empties + 'O' * rocks
        elif line[0] == '#':
            return '.' * empties + 'O' * rocks + '#' + self.move_east(line[1:])
        elif line[0] == '.':
            return self.move_east(line[1:], rocks, empties + 1)
        elif line[0] == 'O':
            return self.move_east(line[1:], rocks + 1, empties)

        # if self.east:
        #     if self.character == 'O':
        #         if self.east.character == '.':
        #             self.character = '.'
        #             self.east.character = 'O'
        #     self.east.move_east()

@lru_cache(maxsize=None)
def fall(line=[], rocks=0, empties=0):
    # print(line)
    if line == '':
        return '.' * empties + 'O' * rocks
    if line[0] == '#':
        return '.' * empties + 'O' * rocks + '#' + fall(line[1:])
    if line[0] == '.':
        return fall(line[1:], rocks, empties + 1)
    if line[0] == 'O':
        return fall(line[1:], rocks + 1, empties)



if __name__ == '__main__':
    line = 'O.#..O.#.#OOO....'
    line = 'O....###..#.............O..O.O..#.O##...O.....#....O..#...O....##.#.O......#..#...O#.O#.##O.O.......'
    characters = []
    for character in line:
        c = Char(character)
        characters.append(c)
        if len(characters) > 1:
            characters[-2].east = c
            # c.east = characters[len(characters) - 2]
    chars = tuple(characters)
    # print(fall(line))
    # exit()
    # print(characters)
    # print(characters[0].get_line())
    # characters[0].move_east()
    # print(characters[0].get_line())

    # blocks = line.split('#')
    # print(blocks)
    # s = [sorted(x) for x in blocks]
    # print(s)
    # exit()
    total_calculaties = 100 * 4 * 1_000_000_000
    timed_calculaties = 10_000
    starttime = timeit.default_timer()
    for _ in range(timed_calculaties):
        fall(line)
        # s = 'O' * 100 + '.' * 4
        # s = 'OOOOOO' + '.....'
        # s = sorted('.............O..O.O..')
        # blocks = line.split('#')
        # # print(blocks)
        # s = [(x.count('O'), len(x)) for x in blocks]
        # # print(s)
        # g = ['.' * (x[1] - x[0]) + 'O' * x[0] for x in s]
        # # print(g)
        # f = '#'.join(g)
        # print(f)
        # characters = chars
        # characters = chars
        # line = characters[0].get_line()
        # # print(line)
        # previous_line = ''
        # while previous_line != line:
        #     previous_line = line
        #     characters[0].move_east()
        #     line = characters[0].get_line()
        #     # print(line)

    diff =  timeit.default_timer() - starttime
    print("The time difference is :", diff)
    print("The calculated uren difference is :", ((diff / timed_calculaties) * total_calculaties) / 3600)
