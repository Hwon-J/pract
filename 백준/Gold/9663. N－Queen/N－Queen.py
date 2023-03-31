def check(tm):
    # 대각선 검사 방법
    # x좌표끼리 뺀값의 절댓값 = y좌표끼리 뺀값의 절댓값 대각선 관계
    for i in range(tm):
        if abs(tm-i)==abs(chess[tm]-chess[i]):
            return 0
    return 1


def queen(num):
    global cnt
    # 퀸을 전부 놓으면 카운트
    if num == N:
        cnt+=1
        return
    # 첫번째 줄부터 하나씩 채우기
    for i in range(N):
        # 방문했다면 continue
        if visit[i]==1:continue
        # 체스의 num번째 줄의 i칸에 퀸을 놓기
        chess[num]=i
        # 놓은 퀸이 대각선 검사를 통과하는지 확인하기
        if check(num):
            # 통과한다면 방문 체크하고 다음줄 퀸 놓기
            visit[i] = 1
            queen(num+1)
            visit[i] = 0



N= int(input())
# 퀸을 놓는 자리를 (인덱스, 값)의 형태로 저장
chess=[-1]*N
visit = [0]*N
cnt=0
queen(0)
print(cnt)