def solution(arr1, arr2):
    s = len(arr1)
    g = len(arr1[0])

    answer = []

    for i in range(s):
        tm = []
        for j in range(g):
            tm.append(arr1[i][j]+arr2[i][j])
        answer.append(tm)
    return answer