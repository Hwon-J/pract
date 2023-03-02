N=int(input())
for i in range(N):
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    cnt = 5
    while cnt>=0:
        if a.count(cnt)==b.count(cnt):
            cnt-=1
            if cnt==0:
                print('D')
                break
        elif a.count(cnt)>b.count(cnt):
            print('A')
            break
        elif a.count(cnt)<b.count(cnt):
            print('B')
            break