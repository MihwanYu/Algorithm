
#Dynamic Programming; 전에 어디 코테에서 이 유형 아예 손도 못댄 적 있어서 문제 안풀고 남들 솔루션 보고 배우는걸 목표로 함
# ref: https://st-lab.tistory.com/141
# 0-1 Knapsack Problem
def solution():
    N,K = map(int, input().split())
    knapsack = []

    # dp: N x K sized table
    dp=[]
    for _ in range(N):
        w,v = map(int, input().split())
        knapsack.append({'wgt':w, 'val':v})
    #최대 K의 무게 안에서 최대 value




if __name__=="__main__":
    solution()