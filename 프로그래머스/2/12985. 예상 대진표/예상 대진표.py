def solution(n,a,b):
    answer = 0
    while 1:
        if a==b:
            break
        if a % 2 == 1:
            a = (a//2) + 1
        elif a % 2 ==0:
            a = a //2
        if b % 2 == 1:
            b = (b//2) + 1
        elif b % 2 ==0:
            b = b //2
        answer+=1

    return answer