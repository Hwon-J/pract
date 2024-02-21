import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
answer = int(21e8)

homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append([i,j])
        elif city[i][j] == 2:
            chickens.append([i,j])

chicken_comb = list(combinations(chickens,M))
for comb in chicken_comb:
    tm_city = 0
    for home in homes:
        tm_home = int(21e8)
        for chicken in comb:
            if (abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])) < tm_home:
                tm_home = abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])
        tm_city += tm_home
    answer = min(answer,tm_city)
print(answer)