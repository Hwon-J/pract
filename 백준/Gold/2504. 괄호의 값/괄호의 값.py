string = input()
stack = []
answer = 0
tm = 1

for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
        tm *= 2
    elif string[i] == '[':
        stack.append('[')
        tm *= 3
    elif string[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if string[i - 1] == '(':
            answer += tm
        stack.pop()
        tm //= 2
    else:
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if string[i - 1] == '[':
            answer += tm
        stack.pop()
        tm //= 3

if stack:
    print(0)
else:
    print(answer)
