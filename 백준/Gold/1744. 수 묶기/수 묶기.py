import sys,heapq
input = sys.stdin.readline

N = int(input())
plus = []
zero = 0
one = 0
minus = []
summ = 0
for _ in range(N):
    a = int(input())
    if a>1:
        heapq.heappush(plus,-a)
    elif a<0:
        heapq.heappush(minus,a)
    elif a==0:
        zero+=1
    elif a == 1:
        one+=1
while len(plus)>1:
    first = -heapq.heappop(plus)
    second = -heapq.heappop(plus)
    summ+=first*second
if plus:
    summ+= -heapq.heappop(plus)

while len(minus)>1:
    first = heapq.heappop(minus)
    second = heapq.heappop(minus)
    summ+= first*second
if minus:
    if zero>0:
        summ+=0
    else:
        summ+= heapq.heappop(minus)
summ+=one
print(summ)