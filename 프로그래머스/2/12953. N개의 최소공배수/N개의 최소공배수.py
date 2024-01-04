def solution(arr):
    answer = 1
    temp = [0]*101
    for num in arr:
        tm = 2
        cnt = 0
        while 1:
            if num == 1:
                break
            if num % tm == 0:
                cnt+=1
                num = num // tm
                temp[tm] = max(temp[tm], cnt)
            else:
                cnt = 0
                tm+=1
    for idx in range(1, 101):
        if temp[idx] != 0:
            answer *= idx**temp[idx]
    return answer