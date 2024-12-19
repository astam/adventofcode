from icecream import ic
import re

if __name__ == '__main__':
    # input_file = '2024/day5/input_example.txt'
    input_file = '2024/day5/input.txt'
    with open(input_file) as f:
        puzzle_input = [x for x in f.read().split('\n')]
    # ic(puzzle_input)

    ordering_rules = [x.split('|') for x in puzzle_input if '|' in x]
    # ic(ordering_rules)
    updates = [x.split(',') for x in puzzle_input if '|' not in x and len(x) > 0]
    # ic(updates)

    correct_updates = 0
    sum = 0
    for update in updates:
        # ic(update)
        correct = True
        middle_index = round(((len(update) + 1) / 2) - 1)
        # ic(middle_index)
        middle = int(update[middle_index])
        # ic(middle)
        for rule in ordering_rules:
            # ic(rule)
            pages = [x for x in update if x in rule]
            # ic(pages)
            if len(pages) == 2:
                if pages[0] == rule[1] and pages[1] == rule[0]:
                    correct = False
        if correct:
            correct_updates += 1
            sum += middle


    ic(correct_updates)
    ic(sum)
