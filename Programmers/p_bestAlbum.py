# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 15:01:21 2021

@author: sally
"""

#장르별 가장 많이 재생된 노래 두개씩
#recognized by id
#기준: 속한노래 가장 많이 재생된 장르-장르 내 가장 많이 재생-횟수 같으면 id낮은노래

#장르: genres, 재생횟수: plays
#def solution: id 순서대로 return

genres = ["classic", "pop", "classic", "classic", "pop", "electric"]
plays = [500, 600, 150, 800, 2500, 4000]
answer=[]
#return: [4, 1, 3, 0]
def solution(genres, plays):
    answer=[]
    songs = {} #dict for {id : {genre : play}}
    
    #step1: filling songs-id로 딕셔너리 만들기
    for i , g in enumerate(genres):
        songs[i] = {g:plays[i]}
    
    g_list = list(set(genres)) #genre types
    g_play={} #dict for {total play : genre}
    for i, g in enumerate(g_list):
        total = sum([i.get(g,0) for i in songs.values()])
        g_play[total] = g
        
    #appending song ids for each genre
    while len(g_play)!= 0:
        #gen: the genre which has the most play counts among remaining counts for genre
        gen = g_play.pop(max(g_play.keys()))
        
        #playnum: id lists among specific genre(gen), sorted descending
        playnum = [i.get(gen) for i in songs.values() if i.get(gen,0) != 0]
        playnum.sort(reverse=True)
        
        #case for only one song exists in specific genre(gen)
        if(len(playnum)==1):
            answer += [i for i in songs if gen in songs[i].keys() and playnum[0] in songs[i].values()]
            continue
        
        #case for only append two songs most frequently played
        for p in playnum[:2]:
            t= [i for i in songs if gen in songs[i].keys() and p in songs[i].values()][0]
            answer.append(t)
            del songs[t]
    return answer


# print(answer)
#첫 실행 결과, test case 2,15에서 틀렸다
#만족못한 것: 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다

print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]))
#문제후기: 모든 장르는 재생된 횟수가 다르다는 조건이 없었으면 골치아플뻔했다.
#장르별 재생횟수를 {재생횟수:장르} 딕셔너리로 만들었는데 동일한 재생횟수가 있었으면 딕셔너리를 다시 디자인해야되니깐..
