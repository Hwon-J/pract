# 학생의 수
N=int(input())
# 학생이 뽑은 번호
lst=list(map(int, input().split()))
# 학생들이 줄선 순서
rlt=[]

student=1
def ans(num):
    global rlt,student
    rlt.insert(len(rlt)-num,student)
    student+=1

for i in range(N):
    ans(lst[i])

print(*rlt)