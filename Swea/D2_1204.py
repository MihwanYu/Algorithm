#최빈수->평균 짐작, 여러개가 최빈수면 가장 큰 점수

T = int(input())
for test_case in range(1, T + 1):
    test_num = int(input())
    print("#%d "%test_num, end='')
    
    frequency=dict()
    scores=map(int, input().split())
    for s in scores:
        if frequency.get(s):
            frequency[s] +=1
        else:
            frequency[s]=1
    # M_freq = max(frequency.values())
    idxes = [idx for idx, val in enumerate(frequency.values()) if val==max(frequency.values())]
    scoreMax = max([list(frequency.keys())[idx] for idx in idxes])
    print(scoreMax)