def dfs(start,summ):
    global cnt
    if summ > K:
        return
    if summ == K:
        cnt += 1
        return
    for i in range(start,N):
        dfs(i+1,summ + A[i])

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    dfs(0,0)
    print(f'#{test_case} {cnt}')