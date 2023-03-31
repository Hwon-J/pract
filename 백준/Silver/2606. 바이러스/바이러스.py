def bfs(num):
    global rlt
    q = []
    q.append(num)
    while q:
        temp = q.pop(0)
        if not temp in rlt:
            rlt.append(temp)
        for i in computer[temp]:
            if visit[i]: continue
            visit[i] = 1
            q.append(i)


# 컴퓨터의 수
N = int(input())
# 연결된 관계의 수
M = int(input())
computer =[[] for _ in range(N+1)]
visit=[0]*(N+1)
rlt=[]
# 인접리스트 만들기
for _ in range(M):
    a,b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

visit[1]=1
bfs(1)
print(len(rlt)-1)