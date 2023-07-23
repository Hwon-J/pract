mx = -21e8  
mn = 21e8   
N = int(input())

number = list(map(int, input().split()))

operator = list(map(int, input().split()))


def dfs(num, idx):
    global mx, mn

    if idx == N:
        mx = max(mx, num)
        mn = min(mn, num)
        return

    for i in range(4):

        if operator[i] > 0:

            operator[i] -= 1

            if i == 0:
                dfs(num + number[idx], idx + 1)
            elif i == 1:
                dfs(num - number[idx], idx + 1)
            elif i == 2:
                dfs(num * number[idx], idx + 1)
            elif i == 3:
                dfs(int(num / number[idx]), idx + 1)

            operator[i] += 1


dfs(number[0], 1)

print(mx)
print(mn)
