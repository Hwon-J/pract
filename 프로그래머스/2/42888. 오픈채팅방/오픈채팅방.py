def solution(record):
    answer = []
    nicknames = {}
    for string in record:
        string = string.split()
        if string[0] == 'Enter':
            nicknames[string[1]] = string[2]
        elif string[0] == 'Change':
            nicknames[string[1]] = string[2]
    for string in record:
        string = string.split()
        if string[0] == 'Enter':
            answer.append(f'{nicknames[string[1]]}님이 들어왔습니다.')
        elif string[0] == 'Leave':
            answer.append(f'{nicknames[string[1]]}님이 나갔습니다.')
    return answer