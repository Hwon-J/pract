# N:색종이의 장수
N=int(input())
paper=[[0]*1001 for _ in range(1001)]

for k in range(N):
    # (a,b)
    a,b,w,h=map(int, input().split())
    for i in range(a,a+w):
        for j in range(b,b+h):
            if i<0 or i>1001 or j<0 or j>1001: continue
            paper[j][i]=k+1


for l in range(N):
    cnt=0
    for m in range(1001):
        for n in range(1001):
            if paper[n][m]==l+1:
                cnt+=1
    print(cnt)