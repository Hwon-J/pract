def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tm = []
        for j in range(len(arr2[0])):
            summ = 0
            for k in range(len(arr1[0])):
                summ += arr1[i][k]*arr2[k][j]
            tm.append(summ)
        answer.append(tm)
    return answer