def solution(queue1, queue2):
    answer = 0
    queWhole = queue1+queue2
    hasAnswer=False
    
    if (sum(queWhole))%2!=0: return -1 #전체 합이 홀수면 바로 리턴-1
    else: queSum =sum(queWhole)//2
    
    for start_idx in range(len(queWhole)):
        dummySum = 0
        answer +=1
        for idx, n in enumerate(queWhole[start_idx:]):
            dummySum += n
            if(dummySum>=queSum): break
        if(dummySum==queSum):
            print('dummy same, answer: ',answer)
            print('the queue1: ',(queWhole[start_idx:start_idx+idx+1]))
            hasAnswer=True
            break
    
    if hasAnswer: return answer               
    return -1


queue1=[1,2,1,2]
queue2=[1,10,1,2]
ans = solution(queue1, queue2)
print(ans)