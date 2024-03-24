def solution(dirs):
    answer = 0
    dir_dict = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visit = set()

    x, y = 0, 0
    for dir in dirs:
        dx, dy = dir_dict[dir]
        nx, ny = x + dx, y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visit.add((x, y, nx, ny))
            visit.add((nx, ny, x, y))
            x, y = nx, ny
    answer = len(visit) // 2
    return answer
