
def ans(i,j):
    summ=arr[i][j]
    for k in range(4):
        dy=i+directy[k]
        dx=j+directx[k]
        if 0<=dy<N and 0<=dx<M:
            summ+=arr[dy][dx]
    return summ

T = int(input())
for test_case in range(1, T + 1):
    N,M=map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    directy=[1,-1,0,0]
    directx=[0,0,1,-1]
    mx=0
    for i in range(N):
        for j in range(M):
            if mx<ans(i,j):
                mx=ans(i,j)

    print(f'#{test_case} {mx}')