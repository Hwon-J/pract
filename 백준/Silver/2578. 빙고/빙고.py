bingo=[list(map(int, input().split())) for _ in range(5)]
call=[list(map(int, input().split())) for _ in range(5)]
# 사회자가 부른 개수
cnt=0
# 빙고 개수
bg=0

# 사회자가 부른 대로 값 변경
def ans(num):
    global cnt
    if cnt>11:
        bg=0
        flag = 0
        for m in range(5):
            if bingo[m][m]!=0:
                flag=1
        if flag == 0:
            bg += 1
        flag = 0
        for m in range(5):
            if bingo[m][4-m]!=0:
                flag=1
        if flag==0:
            bg+=1
        for m in range(5):
            if sum(bingo[m][:5]) == 0:
                bg += 1
        for m in range(5):
            summ=0
            for n in range(5):
                summ+=bingo[n][m]
            if summ==0:
                bg+=1
        if bg>=3:
            return

    for i in range(5):
        for j in range(5):
            if bingo[i][j]==num:
                bingo[i][j]=0
                cnt+=1

# 함수에 하나씩 넣기
for i in range(5):
    for j in range(5):
        ans(call[i][j])
        
print(cnt)