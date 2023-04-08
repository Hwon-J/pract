T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H==0:
        rlt = H*100
        rlt += (N//H)
    else:
        rlt = (N % H)*100
        rlt += (N//H)+1
    print(rlt)