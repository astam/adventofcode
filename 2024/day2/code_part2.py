from icecream import ic

def is_safe(report:list):
    diffs = [j - i for i, j in zip(report, report[1:])]
    if 0 not in diffs:
        if len([x for x in diffs if x > 3 or x < -3]) == 0:
            # ic(report)
            if len([x for x in diffs if x < 0]) > 0 and len([x for x in diffs if x > 0]) > 0:
                return False
            else:
                return True
        else:
            return False
    else:
        return False
    
def is_all_safe(report:list):
    ic(report)
    for i in range(len(report)):
        new = report.copy()
        ic(new.pop(i))
        ic(new)
        if is_safe(new):
            return True
    return False

if __name__ == '__main__':
    # input_file = '2024/day2/input_example.txt'
    input_file = '2024/day2/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    reports = [list(map(int, y)) for y in [x.split(' ') for x in lines]]
    # ic(reports)

    ic(len([x for x in reports if is_all_safe(x)]))
    # for report in reports:
    # is_all_safe(reports[0])