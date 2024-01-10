def solution(arr1, arr2):
    answer = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*arr2)] for X_row in arr1]
    return answer