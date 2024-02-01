def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            tm = numbers[i] + numbers[j]
            if tm not in answer:
                answer.append(tm)
    answer.sort()
    return answer