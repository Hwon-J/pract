from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
mx = 0

for i in permutations(arr):
    tm = 0
    for j in range(1, len(i)):
        tm += abs(i[j] - i[j - 1])
    mx = max(mx, tm)

print(mx)