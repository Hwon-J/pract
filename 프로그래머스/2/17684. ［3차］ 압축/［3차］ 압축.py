def solution(msg):
    answer = []
    alpha_dict = {chr(65+i): i+1 for i in range(26)}
    idx = 27
    i = 0
    while i < len(msg):
        for j in range(i+1, len(msg)+1):
            if msg[i:j] not in alpha_dict:
                answer.append(alpha_dict[msg[i:j-1]])
                alpha_dict[msg[i:j]] = idx
                idx += 1
                i = j - 1
                break
            elif j == len(msg):
                answer.append(alpha_dict[msg[i:j]])
                return answer
    return answer