import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = [0]*(n+1)
for k in range(1, n+1):
    sum_lst[k] = sum_lst[k - 1] + lst[k - 1]
for _ in range(m):
    i, j = map(int, input().split())
    print(sum_lst[j]-sum_lst[i-1])

