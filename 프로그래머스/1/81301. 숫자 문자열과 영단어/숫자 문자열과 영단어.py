def solution(s):
    numbers_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    answer = ""
    tm = ""
    
    for char in s:
        if char.isdigit():  
            answer += char
        else: 
            tm += char
            if tm in numbers_dict:
                answer += numbers_dict[tm]
                tm = ""
    
    return int(answer)
