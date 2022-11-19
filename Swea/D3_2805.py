# NxN 홀수
# 정사각형 마름모 형태 ㅅ확

#농장의 크기 N, 농작물 가치 주어질때 -> 수익은?
# 1<=N<=49, 0<=value<=5

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    values = []
    for _ in range(N):
        row = list(map(int, list(input())))
        values.append(row)

    earnedVal = []

    midN = N//2
    for i, row in enumerate(values):
        start = abs(N//2-i)
        end = N-start
        earnedVal+=row[start:end]
        print(row[start:end])
    # print('earnedVal: ',earnedVal)
    print('#%d %d'%(test_case, sum(earnedVal)))