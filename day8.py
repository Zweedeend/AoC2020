#!/bin/env python3.8
instructions = [(left, int(right)) for left, right in map(str.split, open("day8.txt"))]


def run(instructions):
    visited = set()
    ip = acc = 0
    while ip not in visited:
        visited.add(ip)
        if ip == len(instructions):  # Terminated
            return acc, True
        op, arg = instructions[ip]
        if op == "acc":
            acc += arg
        elif op == "jmp":
            ip += arg - 1
        ip += 1
    return acc, False


print(run(instructions))

for idx in range(len(instructions)):
    original, arg = instructions[idx]
    if original == "acc":
        continue
    new = "jmp" if original == "nop" else "nop"
    instructions[idx] = (new, arg)
    acc, term = run(instructions)
    if term:
        break
    instructions[idx] = (original, arg)

print(acc)
