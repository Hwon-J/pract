def solution(numbers):
    answer = ''
    string_number = list(map(str, numbers))
    string_number.sort(key=lambda x: x * 3, reverse=True)
    answer = str(int(''.join(string_number)))
    return answer