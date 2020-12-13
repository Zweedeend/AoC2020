from functools import reduce
from timeit import Timer


def count(group):
    return reduce(set.union, map(set, group.split()))


groups = open("day6.txt").read().split("\n\n")


def part1():
    questions = map(count, groups)
    return sum(map(len, questions))


print(part1())

questions2 = [reduce(set.intersection, map(set, group.split())) for group in groups]
print(sum(map(len, questions2)))
