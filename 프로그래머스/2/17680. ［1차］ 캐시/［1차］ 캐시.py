from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cities = [city.lower() for city in cities]
    if cacheSize == 0:
        return 5 * len(cities)
    else:
        q = deque()
        for i in range(len(cities)):
            if cities[i] in q:
                if len(q) == cacheSize:
                    q.remove(cities[i])
                q.append(cities[i])
                answer += 1
            else:
                if len(q) == cacheSize:
                    q.popleft()
                q.append(cities[i])
                answer += 5

        return answer
