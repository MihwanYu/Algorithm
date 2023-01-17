# DP 다시풀어야함 -> 처음으로 혼자 성공한 DP,,,흑흑
def solution():
    X = int(input())
    count = 0

    dp = [-1]*(X+1)
    
    dp[X]=0
    dp[X-1]=1
    if X%2==0: dp[X//2]=1
    if X%3==0: dp[X//3]=1

    for i in range(X-1, 0, -1):
        # if i==9: print('dp when i==9: ',dp)
        if dp[i]==-1:
            dp[i] = dp[i+1]+1
        else:
            dp[i] = min(dp[i], dp[i+1]+1)

        if i%2==0:
            if dp[i//2] != -1:
                dp[i//2] = min(dp[i//2], dp[i]+1)
            else:
                dp[i//2] = dp[i]+1

        if i%3==0:
            if dp[i//3] != -1:
                dp[i//3] = min(dp[i//3], dp[i]+1)
            else:
                dp[i//3] = dp[i]+1
        # if i==9: print('dp when i==9: ',dp)
    # print('dp: ',dp)

        
    print(dp[1])
if __name__=="__main__":
    solution()