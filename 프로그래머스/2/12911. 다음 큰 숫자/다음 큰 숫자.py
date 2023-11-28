def solution(n):
    answer = n
    tm = format(n, "b")
    one = tm.count("1")
    while 1:
        answer+=1
        tm2 = format(answer, "b")
        one2 = tm2.count("1")
        if one2 == one:
            break
    return answer