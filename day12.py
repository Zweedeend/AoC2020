import re

example = """F10
N3
F7
R90
F11"""

def solve(text):
    pos = 0
    dir = 1
    for c, nr in re.findall(r'(\w)(\d+)', text):
        nr = int(nr)
        if c == "F":
            pos += dir * nr
        elif c == "L":
            dir *= (1j) ** (nr//90)
        elif c == "R":
            dir *= (-1j) ** (nr//90)
        elif c == "E":
            pos += nr
        elif c == "W":
            pos -= nr
        elif c == "N":
            pos += nr * 1j
        elif c == "S":
            pos -= nr * 1j
    print(pos)
    print(abs(complex(pos).imag) + abs(complex(pos).real))

# solve(example)
solve(open("day12.txt").read())


def waypoint(text):
    wpt = 10 + 1j
    pos = 0
    for c, nr in re.findall(r'(\w)(\d+)', text):
        nr = int(nr)
        if c == "F":
            pos += wpt * nr
        elif c == "L":
            wpt *= (1j) ** (nr//90)
        elif c == "R":
            wpt *= (-1j) ** (nr//90)
        elif c == "E":
            wpt += nr
        elif c == "W":
            wpt -= nr
        elif c == "N":
            wpt += nr * 1j
        elif c == "S":
            wpt -= nr * 1j
    print(pos)
    print(abs(complex(pos).imag) + abs(complex(pos).real))

# print()
# print(waypoint(example))
waypoint(open("day12.txt").read())