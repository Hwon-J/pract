def is_same(word1, word2):
    cnt = sum(w1 != w2 for w1, w2 in zip(word1, word2))
    if cnt == 1:
        return 1
    else:
        return 0

def dfs(begin, target, words, cnt, visit):
    global answer
    if begin == target: 
        answer = min(answer, cnt)
        return
    for word in range(len(words)):
        if is_same(begin,words[word]) and visit[word] == 0:
            visit[word] = 1
            dfs(words[word], target, words, cnt + 1, visit)
            visit[word] = 0

def solution(begin, target, words):
    global answer
    answer = int(21e8)
    if target not in words:
        return 0
    
    visit = [0] * len(words)
    dfs(begin, target, words, 0, visit)
    if answer != 21e8:
        return answer
    else:
        return 0