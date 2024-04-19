from itertools import combinations_with_replacement

n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
answer = combinations_with_replacement(numbers, m)
for i in answer:
    print(*i)