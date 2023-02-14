n=int(input())  # 갑옷 재료 개수
m=int(input())  # 갑옷하나 만드는데 필요한 합
lst=list(map(int, input().split())) # 갑옷 재료 번호 입력
lst.sort()
st=0
ed=n-1
cnt=0

while st<ed:
    if lst[st]+lst[ed]>m:
        ed=ed-1
    elif lst[st]+lst[ed]<m:
        st=st+1
    elif lst[st]+lst[ed]==m:
        cnt+=1
        st+=1
        ed-=1
print(cnt)