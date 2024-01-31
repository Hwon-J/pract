n=int(input())
lst=list(map(int, input().split()))
lst.sort()

cnt=0
# 정렬한 상태이므로 최소 합은 2번째 인덱스이기 떄문에 2부터 시작
for i in range(n):
    target=lst[i]
    st = 0
    ed = n - 1
    while st<ed:
        if lst[st]+lst[ed]==target:
            if st!=i and ed!=i:
                cnt+=1
                break
            elif st==i:
                st+=1
            elif ed==i:
                ed-=1
        elif lst[st]+lst[ed]<target:
            st+=1
        elif lst[st] + lst[ed] > target:
            ed-=1
print(cnt)