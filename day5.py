def parse(line):
    trans = str.maketrans("BRLF", "1100")
    return int(line.translate(trans), 2)
seats = set(map(parse, open("day5.txt")))
myseat = set(range(min(seats), max(seats))) - seats
print(max(seats), myseat)
