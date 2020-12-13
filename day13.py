example = """939
7,13,x,x,59,x,31,19""".splitlines()


def parse(lines):
    lines = iter(lines)
    mine = int(next(lines))
    original = list(map(str.strip, next(lines).split(",")))
    print(original)
    busses = list(map(int, filter(str.isdigit, original)))
    offsets = [original.index(str(bus)) for bus in busses]
    return mine, busses, offsets


def earliest(mine, busses, _):
    wait = [bus - mine % bus for bus in busses]
    best = min(wait)
    bus = next(bus for bus, time in zip(busses, wait) if time == best)
    return (bus, best, bus*best)


print(parse(example))
print(earliest(*parse(example)))
print(earliest(*parse(open("day13.txt"))))

"""
n % 7 = 0
(n+1) % 13 = 0
(n+4) % 59 = 0
(n+6) % 31 = 0
(n+7) % 19 = 0

x % 7 = 0
x % 13 = 1
x % 4 = 59
x % 6 = 31
x % 7 = 19

"""

# Python 3.6
from functools import reduce
from math import gcd

def times(n):
    return reduce(lambda a, b: a * b, n)

def _lcm(a, b):
    return a * b // gcd(a, b)

def lcm(a):
    return reduce(_lcm, a)

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


if __name__ == '__main__':
    n = [7, 13, 59, 31, 19]
    a = [0, 1, 4, 6, 7]
    b = [ni - ai for ni, ai in zip(n, a)]
    print(chinese_remainder(n, b), )
    print(chinese_remainder(n, a) / 1068781 )

"""
x % 7 = 0
x % 13 = 1
x % 4 = 59
x % 6 = 31
x % 7 = 19

"""

def part2(_, busses, offsets):
    modulos = [bus - offset for bus, offset in zip(busses, offsets)]
    return chinese_remainder(busses, modulos)

print(part2(*parse(example)) == 1068781)
print(parse(open("day13.txt")))
print(part2(*parse(open("day13.txt"))))

print(part2(*parse("0\n1789,37,47,1889".splitlines()))==1202161486)
print(part2(*parse("0\n67,7,x,59,61".splitlines()))==1261476)
print(part2(*parse("0\n67,x,7,59,61".splitlines()))==779210)
