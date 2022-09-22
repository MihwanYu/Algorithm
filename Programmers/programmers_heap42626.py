import heapq
#heapify: 리스트-> 힙 리스트 변환(오름차순)
#heappop(리스트) -> 가장 최솟값 반환 및 삭제
#heappush(리스트, 요소) -> 힙 리스트에 요소를 오름차순으로 삽입

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0]>=K: return 0 #최솟값 k보다 크면 바로 리턴

    while scoville[0]<=K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        answer += 1
        if len(scoville)==1 and scoville[0]<K:
            answer = -1
            break
    
    return answer

def solutionFailed(scoville, K):
    #실패 사유: 시간초과 - scoville을 heapq를 사용하지 않고 일반 리스트를 사용함
    answer = 0
    scoville.sort() #오름차순 -> 시간 소요 원인 1
    if min(scoville)>=K: return 0 #min 내장함수 -> 시간 소요 원인 2

    while min(scoville)<=K:
        scoville.insert(0, scoville.pop(0)+ scoville.pop(0)*2) #-> insert: 시간 소요 원인 3
        scoville.sort()
        answer += 1
        if len(scoville)==1 and scoville[0]<K:
            answer = -1
            break
    
    return answer
