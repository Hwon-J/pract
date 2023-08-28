def solution(s):
    answer = True
    s = s.lower()
    np = s.count('p')
    ny = s.count('y')
    if np != ny: answer=False

    return answer