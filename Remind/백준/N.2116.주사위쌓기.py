# 실패
N=int(input())
arr=[list(map(int, input().split())) for _ in range(N)]
maxx=0

def ans(top,summ):
    for i in range(1,N):
        for j in range(6):
            if arr[i][j]==top:
                if j==0:
                    top=arr[i][5]
                    summ += max(arr[i][1:5])
                    break
                elif j == 1:
                    top=arr[i][3]
                    summ += max(arr[i][0], arr[i][2], arr[i][4], arr[i][5])
                    break
                elif j==2:
                    top = arr[i][4]
                    summ += max(arr[i][0], arr[i][1], arr[i][3], arr[i][5])
                    break
                elif j == 3:
                    top=arr[i][1]
                    summ += max(arr[i][0], arr[i][2], arr[i][4], arr[i][5])
                    break
                elif j==4:
                    top = arr[i][2]
                    summ += max(arr[i][0], arr[i][1], arr[i][3], arr[i][5])
                    break
                elif j==5:
                    top=arr[i][0]
                    summ += max(arr[i][1:5])
                    break
    return summ

ret=0
# 첫줄의 원소를 하나씩 윗면으로 두면서 시작
for i in range(6):
    if i==0 or i==5:
        ret=ans(arr[0][i], max(arr[0][1:5]))
    elif i==1 or i==3:
        ret=ans(arr[0][i], max(arr[0][0],arr[0][2],arr[0][4],arr[0][5]))
    elif i==2 or i==4:
        ret=ans(arr[0][i], max(arr[0][0],arr[0][1],arr[0][3],arr[0][5]))

        if ret>maxx:
            maxx=ret
print(maxx)


# 성공
N=int(input())
dice=[list(map(int, input().split())) for _ in range(N)]
# 주사위의 윗면 과 아랫면 딕셔너리 설정
route = {0:5,1:3,2:4,3:1,4:2,5:0}
maxx=0

for i in range(6):
    rlt=[]
    # dice의 자리에 위치한 원소를 삭제
    dice_lst=[1,2,3,4,5,6]
    dice_lst.remove(dice[0][i])
    pair=dice[0][route[i]]
    dice_lst.remove(pair)
    # 남은 수 중에 가장 큰 수 append
    rlt.append(max(dice_lst))
    # 둘째줄부터 for문
    for j in range(1,N):
        dice_lst = [1, 2, 3, 4, 5, 6]
        # 위의 첫번째 과정과 동일
        dice_lst.remove(pair)
        # 사용한 수의 짝 인덱스를 찾기
        # 자리찾기가 헷갈릴 수 있음
        pair= dice[j][route[dice[j].index(pair)]]
        dice_lst.remove(pair)
        rlt.append(max(dice_lst))
    # 최대값 찾기
    ret=sum(rlt)
    if maxx<ret:
        maxx=ret
print(maxx)
