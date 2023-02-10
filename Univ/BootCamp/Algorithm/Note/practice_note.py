# def print_star(num):
#     if num == 1:
#         return print('*')
#     print('*' * num)
#     print_star(num - 1)

import random


# def ary_sum(arr, n):
#     if n <= 0:
#         return arr[0]
#     return arr[n] + ary_sum(ary, n - 1)
#
#
# ary = [random.randint(1, 1000) for _ in range(random.randint(10, 20))]
#
# print(ary)
# print(f'Ary Sum : {ary_sum(ary, len(ary) - 1)}')


# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# for i in range(2, 25):
#     print(fibo(i), end=' ')



pokemons = [
    ("한지우", "피카츄"),
    ("오바람", "꼬부기"),
    ("나이기", "파이리"),
    ("한지우", "파이리"),
    ("덴트", "메더"),
    ("덴트", "암팰리스"),
    ("나이기", "리자드"),
    ("아이리스", "터검니"),
    ("한지우", "이상해")
]

a = dict(pokemons)
print(a)

print(list(a.keys()))

b = dict()

b['a'] = 1
b['a'] += 1
print(b)
