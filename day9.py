from itertools import combinations, islice, accumulate
from collections import deque
from operator import add

example = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]


def possible_sums(preceding):
    return map(sum, combinations(preceding, r=2))

def failure(data, pre_len):
    for idx in range(pre_len, len(data)):
        preceding = data[idx - pre_len:idx]
        item = data[idx]
        if item not in possible_sums(preceding):
            return idx, item


def contiguous(data, pre_len):
    idx, item = failure(data, pre_len)
    for i in range(idx):
        for j in range(i + 1, idx):
            s = sum(data[i:j])
            if s == item:
                return min(data[i:j]) + max(data[i:j])
            if s > item:
                break


print(failure(example, 5))
print(contiguous(example, 5))
print(failure(list(map(int, open("day9.txt"))), 25))
print(contiguous(list(map(int, open("day9.txt"))), 25))


### More functional



def window(data, preamble):
    iterable = iter(data)
    preceding = deque(islice(iterable, preamble), maxlen=preamble)
    for item in iterable:
        yield preceding, item
        preceding.append(item)

def failure2(data, preamble):
    for preceding, item in window(data, preamble):
        if item not in possible_sums(preceding):
            return item
