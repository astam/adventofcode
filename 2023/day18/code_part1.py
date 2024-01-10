from __future__ import annotations
from dataclasses import dataclass
import pysnooper
import sys
from tqdm import tqdm
import turtle
from tkinter import Tk, Canvas, PhotoImage, mainloop

directions = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

width = 1920
height = 1024
window = Tk()
canvas = Canvas(window, width=width, height=height, bg="#000000")
canvas.pack()
img = PhotoImage(width=width, height=height)
canvas.create_image((width//2, height//2), image=img, state="normal")

# def setwindowsize(x=640, y=640):
#     turtle.setup(x, y)
#     turtle.setworldcoordinates(0,0,x,y)

# def drawpixel(x, y, color, pixelsize = 1 ):
#     turtle.tracer(0, 0)
#     turtle.colormode(255)
#     turtle.penup()
#     turtle.setpos(x*pixelsize,y*pixelsize)
#     turtle.color(color)
#     turtle.pendown()
#     turtle.begin_fill()
#     for i in range(4):
#         turtle.forward(pixelsize)
#         turtle.right(90)
#     turtle.end_fill()

# def showimage():
#     turtle.hideturtle()
#     turtle.update()

def print_grid(grid):
    print('\n'.join(grid))
    # print('\n'.join([''.join([y for y in x]) for x in grid]))

def leading_grounds(line):
    splitted = line.split('*')
    # print(splitted[0])
    return '*'.join([' ' * len(splitted[0])] + splitted[1:])

if __name__ == '__main__':
    input_file = '2023/day18/input_example.txt'
    input_file = '2023/day18/input.txt'
    input = open(input_file).read().split('\n')
    # print('\n'.join(input))
    # sys.setrecursionlimit(20000)
    holes = []
    pos_x, pos_y = 0, 0
    for line in input:
        direction, steps, color = line.split()
        # print(pos_x, pos_y, direction, steps, color)
        steps = int(steps)
        dir_x = directions[direction][0]
        dir_y = directions[direction][1]
        if directions[direction][0] != 0:
            new_x = dir_x * steps + pos_x
            holes += [(x, pos_y) for x in range(pos_x, new_x, dir_x)]
            pos_x = new_x
        if dir_y != 0:
            new_y = directions[direction][1] * steps + pos_y
            holes += [(pos_x, y) for y in range(pos_y, new_y, dir_y)]
            pos_y = new_y
    grid = []
    for x in range(min([x for x,y in holes]) - 1, max([x for x,y in holes]) + 2):
        line = ''
        for y in range(min([y for x,y in holes]) - 1, max([y for x,y in holes]) + 2):
            if (x, y) in holes:
                line += '*'
            else:
                line += '.'
        grid.append(line)
    # print_grid(grid)
    # print('\n'.join([''.join([y for y in x]) for x in grid]))
    # print()
    for _ in range(4):
        # print('bla')
        grid = list(map(leading_grounds, map(''.join,zip(*grid[::-1]))))
        # grid = list(map(''.join,zip(*grid[::-1])))
        # grid = map(leading_grounds, grid)
        # print(grid)
    grid = list(map(list, grid))
    for _ in range(8):
        grid = list(map(list, zip(*grid[::-1])))
        for x in range(1, len(grid) - 1):
            for y in range(1, len(grid[x]) - 1):
                if grid[x][y] == '.':
                    if (grid[x][y - 1] == ' ') or (grid[x][y + 1] == ' ') or (grid[x - 1][y] == ' ') or (grid[x + 1][y] == ' '):
                        grid[x][y] = ' ' # = grid[x][:y] + ' ' + grid[x][y + 1:] 

    # print_grid(map(' '.join,grid))
        # print('bla')
    count = 0
    for line in grid:
        count += len([x for x in line if x in '.*'])
    print(count)
    offset = 2
    # setwindowsize(len(grid) + offset, len(grid[0]) + offset)
    # setwindowsize()
    for x in range(len(grid)):
        # print(x)
        for y in range(len(grid[x])):
            # img.put("#ffffff", (x, y))
            if grid[x][y] in '.*':
                if grid[x][y] == ' ':
                    color = 'black'
                elif grid[x][y] == '.':
                    color = 'red'
                else:
                    color = 'white'
                canvas.create_rectangle(x*offset,y*offset,x*offset+offset,y*offset+offset,outline=color, fill=color)
                # print(x,y)
                
                # drawpixel(30, 30, (100,100,100), 10)
                # drawpixel(x + offset, y + offset, color, 10)
    # showimage()
    # turtle.mainloop()
    mainloop()
