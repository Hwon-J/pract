paper=[[0]*101 for _ in range(101)]
for _ in range(4):
    x1,y1,x2,y2=map(int, input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            paper[i][j]=1
cnt=0
for i in range(101):
    for j in range(101):
        if paper[i][j]==1:
            cnt+=1
print(cnt)