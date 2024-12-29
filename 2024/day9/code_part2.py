from icecream import ic
import re
from collections import defaultdict
import sys

class Block():
    def __init__(self):
        self.next = None
        self.previous = None
        self.size = 0

class EmptyBlock(Block):
    def __init__(self, previous, next, size):
        super().__init__()
        self.file_id = None
        self.previous = previous
        self.size = size
        self.next = next
        if next:
            next.previous = self
            
    def defrag(self):
        # if self.previous.file_id == 1:
        #     return
        if self.next:
            if found_file := self.next.get_file(self.size):
                left_space = self.size - found_file.size
                # found_file.next.previous, self.next.previous = self.next.previous, found_file.next.previous
                # found_file.previous.next, self.previous.next = self.previous.next, found_file.previous.next
                found_file.next, self.next = self.next, found_file.next
                found_file.previous, self.previous = self.previous, found_file.previous
                if found_file.previous:
                    found_file.previous.next = found_file
                if found_file.next:
                    found_file.next.previous = found_file
                if self.previous:
                    self.previous.next = self
                if self.next:
                    self.next.previous = self
                self.size = found_file.size
                if left_space > 0:
                    if type(found_file.next) is EmptyBlock:
                        found_file.next.size += left_space
                    else:
                        extra_block = EmptyBlock(found_file, found_file.next, left_space)
                        found_file.next = extra_block
                if self.previous and type(self.previous) is EmptyBlock:
                    self.size += self.previous.size
                    self.previous = self.previous.previous
                    self.previous.next = self
                if self.next and type(self.next) is EmptyBlock:
                    self.size += self.next.size
                    if self.next.next:
                        self.next = self.next.next
                        self.next.previous = self
                
                found_file.defrag()
            else:
                self.next.defrag()

                

        #         if self.previous:
        #             self.previous.next = found_file
        #             found_file.previous = self.previous
        #         left_space = self.size - found_file.size
        #         if left_space == 0:
        #             pass
        #         #     self.next.previous = found_file
        #         #     found_file.next, self.next = self.next, found_file.next
        #         #     found_file.previous, self.previous = self.previous, found_file.previous
        #         #     # found_file.defrag()
        #         else:
        #             extra_block = EmptyBlock(found_file, self.next, left_space)
        #         #     self.next.previous = extra_block
        #             found_file.next = extra_block
        #         #     # extra_block.defrag()
        # else:
        #     return
        #     # self.next.defrag()

    def get_file(self, max_size:int):
        if self.next:
            return self.next.get_file(max_size)
        else:
            return None

    def __str__(self):
        ic(self.file_id)
        if self.next:
            return '.' * self.size + ',' + str(self.next)
        else:
            return '.' * self.size

class FileBlock(Block):
    def __init__(self, pairs:list, file_id:int=0):
        super().__init__()
        self.file_id = file_id
        self.size = pairs[0][0]
        if len(pairs[0]) == 1:
            self.next = None
        elif len(pairs) == 1:
            self.next = EmptyBlock(None, pairs[0][1])
            self.next.previous = self
        else:
            self.next = EmptyBlock(self, FileBlock(pairs[1:], file_id + 1), pairs[0][1])
            
    def defrag(self):
        if self.next:
            self.next.defrag()
        else:
            return

    def get_file(self, max_size:int):
        found_file = None
        if self.next:
            found_file = self.next.get_file(max_size)
        if found_file:
            # ic(self.file_id, found_file.file_id)
            return found_file
        else:
            if self.size <= max_size:
                return self
            else:
                return None
            
    def __str__(self):
        ic(self.file_id)
        if self.next:
            return str(self.file_id) * self.size + ',' + str(self.next)
        else:
            return str(self.file_id) * self.size

if __name__ == '__main__':
    input_file = '2024/day9/input_example.txt'
    # input_file = '2024/day9/input.txt'
    with open(input_file) as f:
        disk_map = list(map(int, f.read()))
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    ic(disk_map)
    pairs = [tuple(disk_map[i:i + 2]) for i in range(0, len(disk_map), 2)]
    ic(pairs)

    sys.setrecursionlimit(20000)
    blocks = FileBlock(pairs)
    print(blocks)
    blocks.defrag()
    # ic(blocks.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.file_id)
    try:
        print(blocks)
    except RecursionError as e:
        ic(e)
