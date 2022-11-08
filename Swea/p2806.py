#NxN board, N queens, 공격하지 못하게 놓는 경우의 수
#공격할 수 있는 방법: 같은 행, 열, 또는 대각선 위

# https://seongonion.tistory.com/103 참고했음,,,다시풀것
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) #N: 1..10
    # print('N: ',N)
    print('#%d '%test_case, end='')
    cases = 0
    queens=[-1]*N

    def isPromising(x):
        for i in range(x):
            if queens[x]==queens[i] or abs(queens[x]-queens[i])==abs(x-i):
                return False
        return True
        # if len(tuple(queens))!=len(queens):
        #     return False #중복 값(col)이 있으면 false 리턴
        # for i, v in enumerate(queens[:-1]):
        #     if v-queens[i+1]==0:
        #         return False
        # return True

    def dfs(lineX):
        #0부터 N-1행까지 모두 성공적으로 돌면서 queen을 배치했으면 case수 1 추가
        global cases
        global queens
        if lineX==N:
            cases+=1
        else:
            # print('queens: ',queens)
            for i in range(N):
                # queens.append(i)
                queens[lineX] = i
                # print('queens: ',queens )
                # 넣을 수 있는 조건 만족하면 true, 다음 row에 값 넣기 진행
                if isPromising(lineX):
                    dfs(lineX+1)
                #조건 거짓이면 방금 전 넣었던 값 다시 빼기
    dfs(0)
    print(cases)


    # for nRow in range(N):
    #     queens=[nRow] #케이스들 중 0번째 행 0에 queen이 있을 경우...N-1행에 queen이 있을 경우
    #     # queens[i] = j -> chess board의 [i][j]에 queen을 넣음
    #     #그다음 1,2,...N행(queens의 idx)에는 기존 queenns의 값과 중복된 값이 들어갈 수 없다(체스판 column uniqueness)
    #     #대각선: 현재보다 아랫줄 확인할 필요x(위부터 채우니까), 위쪽 인덱스와의 관계 확인
        
    #     for nCol in range(N):
    #         if nCol not in queens:
    #             queens.append(nCol)
    