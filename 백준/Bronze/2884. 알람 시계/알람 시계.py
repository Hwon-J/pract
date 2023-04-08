H, M = map(int, input().split())
if M >= 45:
    print(H, M-45)
else:
    if H==0:
        H = 23
    else:
        H-=1
    M = 60-(45-M)
    print(H, M)