string = input()
bomb_str = list(input())

stack = []
for i in range(len(string)):
    stack.append(string[i])
    if stack[-len(bomb_str):] == bomb_str:
        del stack[-len(bomb_str):]
if stack:
    print(''.join(stack))
else:
    print('FRULA')
