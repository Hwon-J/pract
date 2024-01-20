import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        tm1 = heapq.heappop(scoville)
        if tm1 >= K: break
        tm2 = heapq.heappop(scoville)
        heapq.heappush(scoville, tm1+tm2*2)
        answer += 1
    if scoville and scoville[0] < K:
        return -1
    return answer