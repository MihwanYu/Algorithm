
def solution():
    M, N = map(int, input().split())
    dp = [0 if i%2!=0 else -1 for i in range(N+1) ] #홀수: 0 짝수: -1
    dp[1] = -1
    dp[2] = 0
    # 디폴트는 0, 합성수는 모두 -1
    for i in range(3, N+1):
        if dp[i]==-1: continue
        for j in range(2, (N//i)+1):
            dp[i*j] = -1
    for i in range(M, N+1):
        if dp[i]==0:
            print(i)


if __name__=="__main__":
    solution()