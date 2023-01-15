
# 알고리즘 분류: DP ★..
def solution():
    N = int(input())
    costs=[[0,0,0]]
    for _ in range(N):
        costs.append(list(map(int, input().split())))
    dp=[[0,0,0]]
    for i in range(1,N+1):
        # print('i: %d, dp: '%i, dp[i-1], costs[i])
        dp0 = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp1 = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp2 = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        dp.append([dp0, dp1, dp2])

    # print('last cost: ',dp[-1])
    print(min(dp[-1]))
    



if __name__=="__main__":
    solution()