
#Dynamic Programming; 전에 어디 코테에서 이 유형 아예 손도 못댄 적 있어서 문제 안풀고 남들 솔루션 보고 배우는걸 목표로 함
# ref: https://st-lab.tistory.com/141
# 0-1 Knapsack Problem
def solution():
    N,K = map(int, input().split())
    knapsack = []

    # dp: N x K sized table
    # dp=[[0]*(K+1)]*(N+1) <<<< 얕은복사됨, dp[2][5] = 9 만들면 dp[n][5]가 모두 9로바뀜
    dp=[[0]*(K+1) for _ in range(N+1)]
    W=[0]
    V=[0]
    for _ in range(N):
        w,v = map(int, input().split())
        W.append(w)
        V.append(v)
    #최대 K의 무게 안에서 최대 value
    for i in range(1,N+1):
        for j in range(1, K+1):
            
            if W[i]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i - 1][j - W[i]] + V[i])
    print(dp[N][K])

if __name__=="__main__":
    solution()