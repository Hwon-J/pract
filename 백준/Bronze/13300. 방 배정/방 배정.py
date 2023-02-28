#N: 수학여행 참가 학생 수 K:한방 최대 인원
N,K=map(int,input().split())
# 학년별 인원을 넣을 배열 만들기
girl=[0]*7
boy=[0]*7
# 여학생, 남학생 구분하여 배열 채우기
for i in range(N):
    s,g=map(int, input().split())
    if s==0:
        girl[g]+=1
    else:
        boy[g]+=1
# 방의 개수
room=0
for j in range(1,7):
    # 여학생 방 개수 구하기
    if girl[j]==0: pass
    # girl[j]==K인 경우 중복으로 세지는 것을 막기 위해 -1한 값에 서 나눔
    else:
        room+=((girl[j]-1)//K)+1
    # 위와 동일(남학생 방 개수 구하기)
    if boy[j]==0: pass
    else:
        room+=((boy[j]-1)//K)+1
print(room)