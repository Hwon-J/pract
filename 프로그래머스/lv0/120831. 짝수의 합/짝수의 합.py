def solution(n):
    summ=0
    if n % 2==0:
        for i in range(n,0,-2):
            summ+=i
    else:
        for i in range(n-1,0,-2):
            summ+=i
    return summ