
def solution():
    N, K = map(int, input().split())
    countbuy = 0
    while bin(N).count('1') > K:
        idx = bin(N)[::-1].index('1')
        countbuy += 2**idx
        N += 2**idx
    print('물병 최솟값: ',countbuy)

def solution2():
    N, K = map(int, input().split())
    countbuy = 0
    curL = 1
    while N!=K:
        print('N: %d'%N)
        margin = N%2
        N = N//2
        curL *= 2
        if N<K:
            print('불가능: ',-1)
            return
        if margin !=0:
            #마트에서 리터 필요한 만큼 사오기
            # print('구매한 물병: %d'%(curL//2))
            countbuy += (curL//2)
            N += 1
    print('물병 최솟값: ',countbuy)

if __name__=="__main__":
    solution()
