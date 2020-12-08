import re

REQ = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def parse(passport):
    pairs = passport.split()
    return dict(pair.split(":") for pair in pairs)


def valid(passport):
    return all(key in passport for key in REQ)


def more_valid(passport):
    if not (1920 <= int(passport["byr"]) <= 2002):
        return False
    if not (2010 <= int(passport["iyr"]) <= 2020):
        return False
    if not (2020 <= int(passport["eyr"]) <= 2030):
        return False
    if not (match := re.search(r'^(\d+)(cm|in)$', passport['hgt'])):
        return False
    height, unit = match.groups()
    if unit == "cm":
        if not (150 <= int(height) <= 193):
            return False
    elif unit == "in":
        if not (59 <= int(height) <= 76):
            return False
    else:
        return False
    if not re.search(r'^#[a-f0-9]{6}$', passport['hcl'].lower()):
        return False
    if not (passport['ecl'] in "amb blu brn gry grn hzl oth".split()):
        return False
    if not re.match(r'^\d{9}$', passport['pid']):
        return False
    return True


passports = open("day4.txt").read().split("\n\n")
parsed = map(parse, passports)
valid_keys = [passport for passport in parsed if valid(passport)]
valid_count = len(valid_keys)
print(valid_count)
all_valid = map(more_valid, valid_keys)
print(sum(all_valid))
