def solution(n, computers):
    answer =0
    visit = [0]*n
    
    def dfs(i):
        visit[i]=1
        for j in range(n):
            if computers[i][j]==1 and visit[j]==0:
                dfs(j)

    for i in range(n):
        if visit[i]==0:
            dfs(i)
            answer+=1
    return answer