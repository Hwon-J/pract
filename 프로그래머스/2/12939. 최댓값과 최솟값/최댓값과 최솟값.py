def solution(s):
    answer = ''
    lst = list(map(int, s.split(" ")))
    mx = max(lst)
    mn = min(lst)
    answer =  f"{mn} {mx}"
    return answer