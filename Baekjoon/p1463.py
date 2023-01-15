
def solution():
    X = int(input())
    count = 0

    dp = [[X,X,X]]
    i = 0
    while 1 not in dp[-1]:
        ascend = sorted(dp[i])
        dp0 = dp1 = dp2 = -1
        for n in ascend[::-1]:
            if n%3==0:
                dp0 = n//3
            if n%2==0:
                dp1 = n//2
            if n > 1:
                dp2 = n-1
        dp.append([dp0, dp1, dp2])
        print(dp[-1])
        i +=1
        count += 1
        
    print('count: ',count)
if __name__=="__main__":
    solution()