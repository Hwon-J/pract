def solution(arr):
    answer = []
    mn = min(arr)
    if len(arr) == 1:
        answer = [-1]
    else:
        arr.remove(mn)
        answer = arr
    return answer