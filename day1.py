# from itertools import product
# from functools import reduce, partial
# from operator import mul
#
# times = partial(reduce, mul)
#
# numbers = list(map(int, open("day1.txt")))
#
# for repeats in range(2, 4):
#     print(next(times(combo) for combo in product(numbers, repeat=repeats) if sum(combo) == 2020))
#
# # for i in numbers:
# #     for j in numbers:
# #         for k in numbers:
# #             if i + j + k == 2020:
# #                 print(f'{i} + {j} + {k} == 2020')
# #                 print(f'{i} * {j} * {k} == {i*j*k}')
#
#
# # print(next(i * j * k for i in numbers for j in numbers for k in numbers if i + j + k == 2020))
#
# print(next(i * j for i in numbers for j in numbers if i + j == 2020))
#
# print(next(i * j for i in map(int, open("day1.txt")) for j in map(int, open("day1.txt")) if i + j == 2020))

print((lambda numbers: next(i * j for i in numbers for j in numbers if i + j == 2020))(list(map(int, open("day1.txt")))))