def solution(price, money, count):
    answer = -1
    tm = 0
    for i in range(1, count+1):
        tm += price*i
    lack = money - tm
    if lack < 0:
        answer*=lack
    else:
        answer = 0
    return answer