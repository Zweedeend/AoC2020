import re


def parse(line):
    match = re.search(r'^(\d+)-(\d+) (\w): (\w+)', line)
    low, high, let, pas = match.groups()
    return int(low), int(high), let, pas


def check1(tup):
    low, high, let, pas = tup
    return low <= pas.count(let) <= high


def check2(tup):
    low, high, let, pas = tup
    return (pas[low - 1] == let) ^ (pas[high - 1] == let)


lines = [parse(line) for line in open("day2.txt")]
print(sum(map(check1, lines)))
print(sum(map(check2, lines)))

print(sum(map(lambda a:(lambda l,h,k,p:int(l)<=p.count(k)<=int(h))(*re.search(r'^(\d+)-(\d+) (\w): (\w+)',a).groups()),open("day2.txt"))))
print(
    sum(
        map(
            lambda a:
            (lambda l,h,k,p:int(l)<=p.count(k)<=int(h))(
                *re.search(r'^(\d+)-(\d+) (\w): (\w+)',a).groups())
            ,open("day2.txt"))))

print(sum(map(lambda l,h,k,p:int(l)<=p.count(k)<=int(h),*zip(*re.findall(r'(\d+)-(\d+) (\w): (\w+)',open("day2.txt").read())))))


print(sum(map(lambda z:int(z[0])<=z[3].count(z[2])<=int(z[1]),re.findall(r'(\d+)-(\d+) (\w): (\w+)',open("day2.txt").read()))))

#
# def starone(line):
#
#     "1-3 a: abcde"
#     pol, pas = line.split(":")
#     cnt, let = pol.split()
#     low, high = map(int, cnt.split("-"))
#     return low <= pas.count(let) <= high
#
#
# def startwo(line):
#     "1-3 a: abcde"
#     # pol, pas = map(str.strip, line.strip().split(":"))
#     # cnt, let = map(str.strip, pol.strip().split())
#     # low, high = map(int, cnt.split("-"))
#
#     match = re.search(r'^(\d+)-(\d+) (\w): (\w+)', line)
#     low, high, let, pas = match.groups()
#     low, high = map(int, [low, high])
#     # print(low, high, let, pas, pas[low-1], pas[high-1])
#     return ((pas[low - 1] == let) + (pas[high - 1] == let)) == 1
#
#
# print(sum(map(starone, open("day2.txt"))))
# print(sum(map(startwo, open("day2.txt"))))
#
#
# def check1(line):
#     match = re.search(r'^(\d+)-(\d+) (\w): (\w+)', line)
#     low, high, let, pas = match.groups()
#     return bool(re.search(f'{let}{{{low},{high}}}', line))
#
#
# print(sum(map(check1, open("day2.txt"))))
#
