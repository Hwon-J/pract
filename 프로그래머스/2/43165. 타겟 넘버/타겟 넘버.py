answer = 0
def solution(numbers, target):
    global answer
    def dfs(level, summ):
        global answer
        if level == len(numbers):
            if summ == target:
                answer += 1
            return
        dfs(level + 1, summ + numbers[level])
        dfs(level + 1, summ - numbers[level])

    dfs(0, 0)
    return answer