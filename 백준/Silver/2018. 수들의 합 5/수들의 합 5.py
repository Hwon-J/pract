n=int(input())
# 자연수합 개수세기
cnt=0
# 투포인터 값 설정
st,ed=1,1
summ=1
while st<=n:
    if summ==n:
        cnt+=1
        ed+=1
        summ+=ed
    elif summ<n:
        ed+=1
        summ+=ed
    elif summ>n:
        summ-=st
        st+=1
print(cnt)
