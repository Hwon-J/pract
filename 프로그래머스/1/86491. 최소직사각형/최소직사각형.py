def solution(sizes):
    answer = 0
    row = max(map(max, sizes))
    col = max(map(min, sizes))
    answer = (row*col)
    return answer