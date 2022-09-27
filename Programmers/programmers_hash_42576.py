def solution(participant, completion):
    answer = ''
    #동명이인이 여러명 있을 수 있음
    players = dict.fromkeys(participant, 0)
    
    for p in participant:
        players[p] += 1
    for p in completion:
        players[p] -=1
    
    for p in list(players.keys()):
        if players[p]==1:
            answer=p
            break
    
    return answer

#딕셔너리는 속도가 리스트보다 빠르다..
# https://all-knowledge-of-the-world.tistory.com/17
def solutionFailed(participant, completion):
    answer = ''
    for player in completion:
        participant.remove(player) #이거 속도 걸림
    # answer = participant[0]
    return participant[0]