import sys
input = sys.stdin.readline

N = int(input())
lst =[]
for _ in range(N):
    a = input()
    a = a[:-1]
    if a not in lst:
        lst.append(a)
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)
