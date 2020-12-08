grid = open("day3.txt").read().split()
width = len(grid[0])

def angle(h, w):
    return sum(row[i * w % width] == "#"
               for i, row in enumerate(grid[::h]))

part2 = 1
angles = [(1, 3), (1, 5,), (1, 7), (1, 1), (2, 1)]
for trees in [angle(h, w) for h, w in angles]:
    part2 *= trees
print(angle(1, 3), part2)



