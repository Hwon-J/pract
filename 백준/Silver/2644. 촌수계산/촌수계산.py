# n : 사람 수
n = int(input())
# 촌수 계산할 사람
a,b = map(int, input().split())
# 촌수 관계 개수
m = int(input())
# 부모 관계 리스트
relation=[[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)
visit = [0]*(n+1)
rlt = 0
def dfs(num,cnt):
    global rlt
    visit[num] = 1
    if num == b:
        rlt=cnt
        return
    for i in relation[num]:
        if not visit[i]:
            dfs(i,cnt+1)

dfs(a,0)

if rlt==0:
    print(-1)
else:
    print(rlt)