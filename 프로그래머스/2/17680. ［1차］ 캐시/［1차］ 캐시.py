from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return 5 * len(cities)
    else:
        q = deque()
        for i in range(len(cities)):
            tm = cities[i].lower() 
            if tm in q:
                if len(q) == cacheSize:
                    q.remove(tm)
                q.append(tm)
                answer += 1
            else:
                if len(q) == cacheSize:
                    q.popleft()
                q.append(tm)
                answer += 5

        return answer