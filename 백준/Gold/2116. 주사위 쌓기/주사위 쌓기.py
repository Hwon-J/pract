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