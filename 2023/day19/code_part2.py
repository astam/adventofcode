from __future__ import annotations
from dataclasses import dataclass
import pysnooper
import sys
from tqdm import tqdm
import turtle
from tkinter import Tk, Canvas, PhotoImage, mainloop

@dataclass
class Part():
    init_string: str
    state: str = 'in'

    def __post_init__(self):
        self.x, self.m, self.a, self.s = tuple([int(x[1]) for x in map(lambda s: s.split("="), self.init_string[1:-1].split(','))])
        self.total_rating = self.x + self.m + self.a + self.s

@dataclass
class Workflow():
    init_string: str

    def __post_init__(self):
        self.name = self.init_string[:self.init_string.index('{')]
        self.rules = self.init_string[self.init_string.index('{') + 1:-1].split(',')
        print(self.rules)

    def transit(self, part: Part):
        for rule in self.rules:
            if ':' not in rule:
                part.state = rule
            else:
                evaluation, state = rule.split(':')
                evaluation = 'part.' + evaluation
                if eval(evaluation):
                    part.state = state
                    break


workflows = {}

if __name__ == '__main__':
    input_file = '2023/day19/input_example.txt'
    # input_file = '2023/day19/input.txt'
    input = open(input_file).read().split('\n')
    parts = list(map(Part, input[input.index('') + 1:]))
    workflows = {x.name:x for x in map(Workflow, input[:input.index('')])}
    # print(parts)
    # print(workflows)
    while len([x for x in parts if x.state not in 'RA']) > 0:
        for part in parts:
            if part.state not in 'RA':
                workflows[part.state].transit(part)

    print(sum([x.total_rating for x in parts if x.state in 'A']))
            
possibilities {
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000)
}
