def solution(genres, plays):
    answer = []
    song_cnt = {}
    song_list = {}
    for i in range(len(genres)):
        if genres[i] not in song_cnt:
            song_cnt[genres[i]] = plays[i]
        else:
            song_cnt[genres[i]] += plays[i]
        if genres[i] not in song_list:
            song_list[genres[i]] = [[plays[i],i]]
        else:
            song_list[genres[i]].append([plays[i],i])
            
    song_cnt = dict(sorted(song_cnt.items(), key = lambda x:x[1], reverse = True))
    
    for genre, _ in song_cnt.items():
        song_list[genre] = sorted(song_list[genre], key=lambda x: (-x[0], x[1]))
        if len(song_list[genre]) > 1:
            answer.append(song_list[genre][0][1])
            answer.append(song_list[genre][1][1])
        else:
            answer.append(song_list[genre][0][1])
    return answer