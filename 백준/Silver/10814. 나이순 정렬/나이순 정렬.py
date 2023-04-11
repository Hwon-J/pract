import sys
input = sys.stdin.readline
lst =[]
N = int(input())
for i in range(N):
    a , b = input().split()
    lst.append([int(a),b])
rlt = sorted(lst, key=lambda x:x[0])
for i in rlt:
    print(*i)