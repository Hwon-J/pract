def solution(s):
    answer = False
    tm = list(s)
    tm.sort()
    if len(tm)==4 or len(tm)==6:
        if ord(tm[-1])<65:
            answer = True
    return answer