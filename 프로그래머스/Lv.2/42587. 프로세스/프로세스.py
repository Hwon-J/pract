from collections import deque

def solution(priorities, location):
    answer = 0
    priority_location = deque([(i, p) for i, p in enumerate(priorities)])
    
    while priority_location:
        current = priority_location.popleft()
        max_priority = max(priority_location, key=lambda x: x[1], default=(0, 0))[1]

        if current[1] >= max_priority:
            answer += 1
            if current[0] == location:
                break
        else:
            priority_location.append(current)

    return answer
