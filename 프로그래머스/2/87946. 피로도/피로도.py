answer = 0  
def DFS(k, cnt, dungeons, visit):
    global answer
    if answer < cnt:  
        answer = cnt
    
    for i in range(len(dungeons)):
        if visit[i] == 0 and k >= dungeons[i][0]:
            visit[i] = 1  
            DFS(k - dungeons[i][1], cnt + 1, dungeons, visit)
            visit[i] = 0  

def solution(k, dungeons):
    global answer
    visit = [0] * len(dungeons)
    DFS(k, 0, dungeons, visit)
    return answer
