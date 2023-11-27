def solution(s):
    answer = True
    stack = []
    for i in s:
        if not stack:
            if i== "(":
                stack.append(i)
            else:
                answer = False
                break
        else:
            if i== "(":
                stack.append(i)
            else:
                stack.pop()
    if len(stack)>=1:
        answer = False
                

    return answer