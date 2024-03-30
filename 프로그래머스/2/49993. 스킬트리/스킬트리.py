from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skills = deque(skill)
        flag = 1
        for s in skill_tree:
            if s in skills:
                if s != skills[0]:
                    flag = 0
                    break
                else:
                    skills.popleft()
        if flag:
            answer += 1
    return answer