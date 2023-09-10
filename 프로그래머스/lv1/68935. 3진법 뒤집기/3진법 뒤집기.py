def solution(n):
    answer = 0
    three = ''
    while n > 0:
        rest = n % 3
        n = n // 3
        three += str(rest)
    answer = int(three,3)
    return answer