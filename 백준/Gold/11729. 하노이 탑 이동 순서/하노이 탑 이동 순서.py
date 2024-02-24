def hanoi(n, st, ed):
    if n == 1:
        print(st, ed)
    else:
        tm = 6 - st - ed
        hanoi(n-1, st, tm)
        print(st, ed)
        hanoi(n-1, tm, ed)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3)
