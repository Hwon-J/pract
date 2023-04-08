import sys
input = sys.stdin.readline
mx,idx = 0,0
for i in range(9):
    a = int(input())
    if a>mx:
        mx = a
        idx = i
print(mx)
print(idx+1)