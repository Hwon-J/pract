def solution(num_list):
    answer = 0
    summ = sum(num_list)
    mul = 1
    for i in num_list:
        mul*=i
    if mul < summ**2:
        answer = 1
    return answer