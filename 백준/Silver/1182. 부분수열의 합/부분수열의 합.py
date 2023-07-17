from itertools import combinations

n, s = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
# 1 - n+1개까지 모든 조합 구하기
for i in range(1, n+1):
    tm = combinations(lst, i)
    # 만들어진 조합의 합을 구해서 s와 비교해서 cnt+1
    for j in tm:
        if sum(j) == s:
            cnt += 1

print(cnt)