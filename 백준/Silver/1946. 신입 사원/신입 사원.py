import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort()
    cnt = 1
    tm = rank[0][1]
    for i in range(1, n):
        if rank[i][1] < tm:
            tm = rank[i][1]
            cnt += 1
    print(cnt)