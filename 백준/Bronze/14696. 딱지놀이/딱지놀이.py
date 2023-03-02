# N: 딱지게임 라운드 수
N=int(input())
for i in range(N):
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    alst=[0]*5
    blst=[0]*5
    for j in a:
        alst[j]+=1
    for k in b:
        blst[k]+=1
    cnt = 4
    while cnt>=0:
        if alst[cnt]==blst[cnt]:
            cnt-=1
            if cnt==0:
                print('D')
                break
        elif alst[cnt]>blst[cnt]:
            print('A')
            break
        elif alst[cnt]<blst[cnt]:
            print('B')
            break