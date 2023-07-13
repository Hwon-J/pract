def solution(name):

    answer = 0
    left_right = len(name) - 1

    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)

        n = i + 1

        while n < len(name) and name[n] == 'A':
            n += 1

        new_left_right = i + len(name) - n + min(len(name) - n, i)

        left_right = min(left_right, new_left_right)

    return answer + left_right

