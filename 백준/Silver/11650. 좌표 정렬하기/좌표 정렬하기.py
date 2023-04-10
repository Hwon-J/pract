N = int(input())
lst =[]
for _ in range(N):
    x,y = map(int, input().split())
    lst.append([x,y])
arr = sorted(lst, key=lambda x:(x[0],x[1]))
for i in arr:
    print(*i)