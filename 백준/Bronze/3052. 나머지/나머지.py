import sys
input = sys.stdin.readline
rlt = []
for _ in range(10):
    a = int(input())
    tm = a % 42
    if tm not in rlt:
        rlt.append(tm)
print(len(rlt))