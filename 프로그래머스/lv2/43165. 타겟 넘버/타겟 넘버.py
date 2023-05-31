def solution(numbers, target):
    answer = 0
    def dfs(level, summ):
        nonlocal answer
        if level == len(numbers):
            if summ == target:
                answer += 1
            return
        dfs(level + 1, summ + numbers[level])
        dfs(level + 1, summ - numbers[level])

    dfs(0, 0)
    return answer