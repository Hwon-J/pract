import heapq

def solution(n, works):
    answer = 0
    works_heap = []
    for work in works:
        heapq.heappush(works_heap,-work)
    while n > 0:
        tm = -heapq.heappop(works_heap)
        if tm == 0: break
        tm -= 1
        n -= 1
        heapq.heappush(works_heap,-tm)
    print(works_heap)
    for work in works_heap:
        answer += work**2
    return answer