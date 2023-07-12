S = input()
T = input()

while True:
    if T == S:
        print(1)
        break
    if len(T) <= len(S):
        print(0)
        break
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]