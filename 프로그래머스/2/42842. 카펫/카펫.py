def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            j = yellow // i
            tm = (j+i)*2 + 4
            if tm == brown:
                answer = [j+2,i+2]
                break
    return answer