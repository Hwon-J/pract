import sys
input = sys.stdin.readline

N = int(input())
arr = []
cnt = 1
for i in range(N):
    s,e = map(int, input().split())
    arr.append([s,e])
arr.sort()
lst = sorted(arr, key=lambda x:x[1])

end = lst[0][1]
for i in range(1, N):
    if lst[i][0] >= end:
        cnt+=1
        end = lst[i][1]
print(cnt)