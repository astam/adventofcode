# https://www.youtube.com/watch?v=g3Ms5e7Jdqo
from functools import lru_cache

@lru_cache(maxsize=None)
def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if "#" in cfg else 1
    
    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
    
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and '.' not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    return result
    

if __name__ == '__main__':
    input_file = '2023/day12/input_example.txt'
    input_file = '2023/day12/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)

    total = 0
    for line in lines:
        cfg, nums = line.split()
        cfg = '?'.join([cfg] * 5)
        nums = ','.join([nums] * 5)
        nums = tuple(map(int, nums.split(',')))
        # print(nums, cfg)
        total += count(cfg, nums)

    print(total)