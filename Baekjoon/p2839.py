
def solution():
    N = int(input())

    dp = [-1]*(N+1)
    for i in range(1, N+1):
        if i%3==0: dp[i] = i//3
        if i%5==0: dp[i] = i//5
    for i in range(7, N+1):
        if dp[i-3] !=-1:
            dp[i] = dp[i-3]+1
        if dp[i-5] !=-1:
            dp[i] = min(dp[i], dp[i-5]+1)
    # print(dp)
    print(dp[N])

if __name__=="__main__":
    solution()