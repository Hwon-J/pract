N , M = map(int, input().split())
card = list(map(int, input().split()))
mn = 21e8
ans = 0
def dfs(level, start,summ):
    global mn,ans
    if level==3:
        if summ > M:return 
        if mn> M-summ:
            mn = M-summ
            ans = summ
        return

    for i in range(start,N):
        dfs(level+1,i+1,summ+card[i])

dfs(0,0,0)
print(ans)