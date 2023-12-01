input_file = '2020/day3/input_example.txt'
input_file = '2020/day3/input.txt'
with open(input_file) as f:
    lines = [line.strip() for line in f.readlines()]
# print(lines)

grid_width = len(lines[0])
# print(grid_width)

# Part 1
right = 3
down = 1
trees = 0
for line_number in range(0, len(lines), down):
    if lines[line_number][(line_number * right) % grid_width] == '#':
        trees += 1
print(trees)

# Part 2
trees = []
product = 1
for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    right, down = slope
    print(slope)
    tree_count = 0
    for line_number in range(0, len(lines), down):
        print(lines[line_number])
        if lines[line_number][(round(line_number * right / down)) % grid_width] == '#':
            tree_count += 1
    trees.append(tree_count)
    product *= tree_count
print(trees)
print(product)
