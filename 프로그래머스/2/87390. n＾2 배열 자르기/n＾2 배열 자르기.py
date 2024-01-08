def solution(n, left, right):
    answer = []
    st_row = left // n
    ed_row = right // n
    for i in range(st_row, ed_row + 1):
        for j in range(n):
            if i >= j:
                answer.append(i+1)
            else:
                answer.append(j+1)
    st_point = left % n
    ed_point = right - (n*st_row)
    answer = answer[st_point:ed_point+1]
    return answer