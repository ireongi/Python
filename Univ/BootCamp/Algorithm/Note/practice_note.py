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


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(2, 25):
    print(fibo(i), end=' ')