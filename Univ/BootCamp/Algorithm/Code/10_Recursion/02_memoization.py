memo = list()


def fibo_memo(n):
    global memo
    memo = [1, 1]

    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n + 1):
            memo.append(memo[i - 1]+memo[i - 2])
        return memo[n]


def fibo_recu(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recu(n - 1) + fibo_recu(n - 2)


print('Fibonacci : ', end='')
for i in range(2, 40):
    print(f'{i} : {fibo_memo(i)}')
print()
print('Iterator : ', end='')
for i in range(2, 40):
    print(f'{i} : {fibo_recu(i)}')
