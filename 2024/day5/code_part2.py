from icecream import ic
import re
from functools import cmp_to_key

def compare(a, b):
    if (a, b) in ordering_rules:
        return 1
    elif (b, a) in ordering_rules:
        return -1
    else:
        return 0

ordering_rules = []

if __name__ == '__main__':
    # input_file = '2024/day5/input_example.txt'
    input_file = '2024/day5/input.txt'
    with open(input_file) as f:
        puzzle_input = [x for x in f.read().split('\n')]
    # ic(puzzle_input)

    ordering_rules = [tuple(x.split('|')) for x in puzzle_input if '|' in x]
    # ic(ordering_rules)
    updates = [x.split(',') for x in puzzle_input if '|' not in x and len(x) > 0]
    # ic(updates)

    correct_updates = 0
    incorrect_updates = 0
    correct_sum = 0
    incorrect_sum = 0
    for update in updates:
        # ic(update)
        correct = True
        middle_index = round(((len(update) + 1) / 2) - 1)
        # ic(middle_index)
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
            middle = int(update[middle_index])
            correct_sum += middle
        else:
            incorrect_updates += 1
            sorted_incorrect_updates = sorted(update, key=cmp_to_key(compare))
            middle = int(sorted_incorrect_updates[middle_index])
            incorrect_sum += middle



    ic(correct_updates)
    ic(correct_sum)
    ic(incorrect_updates)
    ic(incorrect_sum)
