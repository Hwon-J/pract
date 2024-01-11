def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        remain = int(((100-progresses[i]-0.1) // speeds[i])+1)
        if not days:
            days.append(remain)
        else:
            if days[0] < remain:
                answer.append(len(days))
                days=[remain]
            else:
                days.append(remain)
    answer.append(len(days))
    return answer