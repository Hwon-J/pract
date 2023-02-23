from collections import deque
T=int(input())
for test_case in range(1,T+1):
    # V: 노드의 개수, E: 간선의 개수
    V,E= map(int,input().split())
    # 간선 정보
    lst=[list(map(int, input().split())) for _ in range(E)]
    # S: 시작, G:끝
    S,G= map(int, input().split())
    # 인접행렬 만들기
    arr=[[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        arr[lst[i][0]][lst[i][1]]=1
        arr[lst[i][1]][lst[i][0]]=1
    # 방문 표시 배열 만들기
    visit=[0]*(V+1)
 
    def bfs(st):
        q=deque()
        q.append((st,0))
    # 튜플로 숫자와 cnt를 한번에 받기
        while q:
            now,cnt=q.popleft()
 
            for i in range(1,V+1):
                if arr[now][i]==1:
                    if visit[i]==0:
                        visit[i]=1
                        if visit[G] == 1:
                            return cnt+1
                        q.append((i,cnt+1))
        else:
            return 0
 
 
    visit[S]=1
    ret=bfs(S)
    print(f'#{test_case} {ret}')
