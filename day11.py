example = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()


def is_chair(char):
    return char == "L"


chairs = {(row, col): False
          for row, line in enumerate(open("day11.txt"))
          # for row, line in enumerate(example)
          for col, char in enumerate(line.strip())
          if is_chair(char)}


def neighbors(pos):
    x, y = pos
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            yield x + dx, y + dy


def surrounding(pos, grid):
    return sum(grid.get(bor, False) for bor in neighbors(pos))

def can_see(pos, grid, maxtries):
    x, y = pos
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            for attempt in range(1, maxtries+1):
                new_pos = x + attempt * dx, y + attempt * dy
                if new_pos in grid:
                    yield grid[new_pos]
                    break

def surrounding_see(pos, grid, maxtries):
    return sum(can_see(pos, grid, maxtries))



def rule1(chair, bors):
    if chair and bors >= 4:
        return False
    if (not chair) and bors == 0:
        return True
    return chair

def rule2(chair, bors):
    if chair and bors >= 5:
        return False
    if (not chair) and bors == 0:
        return True
    return chair

def evolve(grid):
    new_grid = {
        pos: rule1(chair, surrounding(pos, grid))
        for pos, chair in grid.items()
    }
    return new_grid

def evolve2(grid):
    maxtries = max(max(grid))
    new_grid = {
        pos: rule2(chair, surrounding_see(pos, grid, maxtries))
        for pos, chair in grid.items()
    }
    return new_grid


last = -1
while (occu := sum(chairs.values())) != last:
    chairs = evolve(chairs)
    last = occu
print(sum(chairs.values()))

chairs = {(row, col): False
          for row, line in enumerate(open("day11.txt"))
          # for row, line in enumerate(example)
          for col, char in enumerate(line.strip())
          if is_chair(char)}

last = -1
while (occu := sum(chairs.values())) != last:
    chairs = evolve2(chairs)
    last = occu
print(sum(chairs.values()))