# 1옆이 0이면 그 부분이 경계이므로 경계 값을 2로 변경해주기
def ans(y,x):
    global cnt
    temp=0
    for k in range(4):
        dy=y+directy[k]
        dx=x+directx[k]
        # 범위 내이고 1인 자리를 가져왔으므로 dy,dx는 0값을 가지고 있어야함
        if 0<=dy<101 and 0<=dx<101:
            if paper[dy][dx]==0:
                paper[y][x]=2
                cnt+=1


paper=[[0]*101 for _ in range(101)]
# N: 색종이 수
N=int(input())
# 둘레의 길이
cnt=0
# 색종이 자리 입력 받아 범위 1로 채우기
for _ in range(N):
    a,b=map(int, input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            paper[i][j]=1
directy=[0,0,1,-1]
directx=[1,-1,0,0]

for m in range(101):
    for n in range(101):
        if paper[m][n]==1:
            ans(m,n)

print(cnt)
