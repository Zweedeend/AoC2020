import re
from collections import defaultdict

def parse(line):
    line = re.sub(r' bags?', '', line)
    left, right = line.split(" contain ")
    rules = {bag: int(cnt) for cnt, bag in re.findall(r'(\d+) ([^,.]+)', right)}
    return left, rules


def flood(edge, flooded):
    if not edge:
        return flooded
    new = {key for key, value in rules.items() if any(set(value) & edge)} - flooded
    return flood(new, flooded | new)




def nest(bag):
    return 1 + sum(count * nest(inner) for inner, count in rules[bag].items())


rules = dict(map(parse, open("day7.txt")))
inverse = {}
for outer, rule in rules.items():
    for inner in rule:
        inverse.setdefault(inner, []).append(outer)

def grow(bag, bags):
    bags.add(bag)
    if bag not in inverse:
        return bags
    for outer in inverse[bag]:
        grow(outer, bags)
    return bags

print("grow", len(grow('shiny gold', set())))

print(inverse)
print(len(flood({'shiny gold'}, set())))
print(nest('shiny gold') - 1)
