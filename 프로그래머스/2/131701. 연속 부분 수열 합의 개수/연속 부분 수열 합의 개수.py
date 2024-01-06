def solution(elements):
    answer = 0
    length = len(elements)
    tm_lst = elements * 2
    sum_lst = set(elements)
    for num in range(2,length):
        tm_sum = sum(tm_lst[:num])
        sum_lst.add(tm_sum)
        for j in range(length-1):
            tm_sum-=tm_lst[j]
            tm_sum+=tm_lst[j+num]
            sum_lst.add(tm_sum)
    answer = len(sum_lst)+1
    return answer