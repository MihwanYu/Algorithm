import math
def solution():
    # 서쪽에 N, 동쪽에 M개의 Site. 
    # 다리끼리는 서로 겹쳐질 수 없을 때 N개 다리를 지을 수 있는 경우의 수
    N, M = map(int, input().split())

    # count = NMcases(N,M)
    # nCk = n! / k!(n-k)!
    # nCk로 풀수있는 이유) 다리 m개중에 n개만 고르면 어차피 교차할 일이 없다
    count = nCk(M,N)
    print('count: %d'%count)

def nCk(M,N):
    c = math.factorial(M) //( math.factorial(N) * math.factorial(M-N) )
    return c

def NMcases(N,M):
    if N==M:
        return 1
    if N==1:
        return M
    diff = M-N
    if diff==1:
        return M
    counts = 0
    for d in range(diff):
        count = NMcases(N-1, M-d-1)
    #     #3 6, 3 5, 3 4, 3 3
        counts += count
    print('N: %d, M: %d, counts: %d'%(N,M,counts))
    return counts




if __name__=="__main__":
    testcase = int(input())
    for case in range(testcase):
        solution()