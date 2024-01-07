def solution(s):
    answer = 0
    length = len(s)
    for i in range(length):
        tm_string = s[i:]+s[:i]
        stack = []
        flag = 1
        for idx in range(length):
            if not stack and tm_string[idx] in [']', '}', ')']: 
                flag = 0
                break
            if tm_string[idx] in ['[', '{', '(']:
                stack.append(tm_string[idx])
            elif stack[-1] == '(':
                if tm_string[idx] == ')':
                    stack.pop()
                else: 
                    flag = 0
                    break
            elif stack[-1] == '{':
                if tm_string[idx] == '}':
                    stack.pop()
                else: 
                    flag = 0
                    break
            elif stack[-1] == '[':
                if tm_string[idx] == ']':
                    stack.pop()
                else: 
                    flag = 0
                    break
        if not stack and flag:
            answer+=1          
    return answer