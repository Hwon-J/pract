import heapq

N = int(input())
card = []
for i in range(N):
    a = int(input())
    heapq.heappush(card,a)
total = 0

while (len(card)>1):
    tm1= heapq.heappop(card)
    tm2 = heapq.heappop(card)
    total+=(tm1+tm2)
    heapq.heappush(card, tm1+tm2)

print(total)