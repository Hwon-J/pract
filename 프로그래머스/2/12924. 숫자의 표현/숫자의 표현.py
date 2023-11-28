def solution(n):
    answer = 1
    arr =[]
    tm = 1
    while 1:
        summ = sum(arr)
        if summ == n:
            answer += 1
        if summ <= n:
            arr.append(tm)
            tm += 1
        else:
            arr.pop(0) 
        if tm > n:
            break
    
    return answer