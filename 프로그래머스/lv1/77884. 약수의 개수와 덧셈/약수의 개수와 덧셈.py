def solution(left, right):
    def divisor(n):
        cnt = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                cnt += 2
        if int(n**0.5)**2 == n:
            cnt -= 1
        return cnt
    
    answer = 0
    for n in range(left, right+1):
        tm = divisor(n)
        if tm % 2 == 0:
            answer += n
        else:
            answer -= n
            
    return answer