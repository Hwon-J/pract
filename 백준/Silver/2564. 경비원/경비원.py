G,S=map(int, input().split())
N=int(input())
shop=[list(map(int, input().split())) for _ in range(N)]
nowD,nowL=map(int, input().split())
total=0
def ans(D,L):
    global total
    if D == nowD:
        total+=abs(L-nowL)
    else:
        if (D==1 and nowD==2) or (D==2 and nowD==1):
            temp=min((L+nowL+S),(G*2-L-nowL+S))
            total+=temp
        elif (D==1 and nowD==3) or (D==3 and nowD==1):
            total+=nowL
            total+=L
        elif D==1 and nowD==4:
            total+=(G-L)
            total+=nowL
        elif D==2 and nowD==3:
            total+=L
            total+=(S-nowL)
        elif D==2 and nowD==4:
            total+=(G-L)
            total+=(S-nowL)
        elif D==3 and nowD==2:
            total+=(S-L)
            total+=nowL
        elif (D==3 and nowD==4) or (D==4 and nowD==3):
            temp=min((L+nowL+G),(S*2-L-nowL+G))
            total+=temp
        elif D==4 and nowD==1:
            total+=L
            total+=(G-nowL)
        elif D==4 and nowD==2:
            total+=(S-L)
            total+=(G-nowL)

for i in range(N):
    ans(shop[i][0],shop[i][1])
print(total)