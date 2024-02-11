import math

def solution(n, stations, w):
    answer = 0
    able = []

    for station in stations:
        st = max(1, station - w)
        ed = min(n, station + w)
        able.append([st, ed])

    answer += math.ceil((able[0][0]-1)/(w*2+1))
    answer += math.ceil((n-able[-1][1])/(w*2+1))
    for i in range(len(able)-1):
        tm = able[i+1][0] - able[i][1]-1
        answer += math.ceil(tm/(w*2+1))
    return answer


