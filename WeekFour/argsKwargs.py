def function(*args):
    """
    param : anything
    return : none
    """
    for name in args:
        print(name)

nums = [[1,1],[2,3],[3,4]]

nums = list(map(set, nums))

print(nums)

nums = [1,2,3,3,3,4,5]

print(list(filter(lambda x : x != 3, nums)))

from functools import reduce

help(reduce)

2023-12-122023-12-12