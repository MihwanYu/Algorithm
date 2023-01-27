#dfs vs 소요시간짧은순대로 - 시간초과 나던말던 그냥 dfs 해보고싶었음 
# 람다 다중조건 설정하기 https://dailyheumsi.tistory.com/67 ★

def solution():
    N = int(input())
    conf=[list( map(int, input().split())) for _ in range(N) ]
    conf.sort(key=lambda x: (x[1], x[0])) # 정렬기준2개: 끝나는 시간 빠를수록 -> 시작하는 시간 빠를수록
    #가장 마지막 시간
    endmax = max([con[1] for con in conf])
    timetable = [-1 for i in range(endmax+1)]

    count = 0
    # time = conf[0][1] #끝시간
    time = 0
    for con in conf:
        if con[0]>=time: #회의 시작할 수 있을 때
            count +=1
            time = con[1]
    print(count)

    # print(max([c1,c2]))
    
    #conf: 주어진 회의 리스트, start: 시작 시간, cumm: 누적된 회의 수, maxc: 가능한 최대 회의 수
def dfs(conf, start, cumm, maxc):
    if len(conf)==1:#회의 리스트 1갠데 회의 시작 시간보다 start 가 작으면 회의 가능하니까 마지막 회의도 추가
        if conf[0][0]>=start:
            cumm +=1
        if cumm>maxc:
            maxc = cumm
        return maxc
    count = 0
    
    #주어진 시작 시간(4)보다 회의 리스트의 시작 시간이 작으면(3) 그 회의를 건너뛰고 다음 회의 추가할 수 있는지 확인
    if start>conf[0][0]:
        cnt = dfs(conf[1:], start, cumm, maxc)
    else:
        #회의 리스트를 추가할 수 있을 때 추가할지 / 안할지 2가지 선택지 중 더 나은 선택지 고르기
        cnt1 = dfs(conf[1:], conf[0][1], cumm+1, maxc)
        cnt2 = dfs(conf[1:],start, cumm, maxc)
        cnt = max(cnt1, cnt2)

    return cnt
        

if __name__=="__main__":
    solution()