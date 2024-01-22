import sys
input = sys.stdin.readline

def solution(x1, y1, x2, y2, accumulate_table):
    answer = accumulate_table[x2][y2] - accumulate_table[x2][y1-1] - accumulate_table[x1-1][y2] + accumulate_table[x1-1][y1-1]
    return answer

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]
accumulate_table = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        accumulate_table[i][j] = table[i-1][j-1] + accumulate_table[i-1][j] + accumulate_table[i][j-1] - accumulate_table[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(solution(x1, y1, x2, y2, accumulate_table))
