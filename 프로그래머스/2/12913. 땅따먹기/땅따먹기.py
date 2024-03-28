def solution(land):
    dp = land[0]
    for i in range(1, len(land)):
        tm = [0] * 4
        for j in range(4):
            for k in range(4):
                if j != k:
                    tm[j] = max(tm[j], dp[k] + land[i][j])
        dp = tm
    return max(dp)