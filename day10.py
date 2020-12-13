import numpy as np
from collections import Counter

numbers = list(map(int, open("day10.txt")))
numbers = [0] + numbers + [max(numbers) + 3]
cnt = Counter(np.diff(np.array(sorted(numbers))))
print(cnt[1] * cnt[3])

ways = {0: 1}
for ada in sorted(numbers[1:]):
    ways[ada] = ways.get(ada - 1, 0) + ways.get(ada - 2, 0)\
                + ways.get(ada - 3, 0)
print(ways[max(numbers)])
