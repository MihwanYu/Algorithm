
def solution():
    fiboN = int(input())
    zeros = [1,0,1]
    ones = [0,1,1]
    #fiboN 커질때마다 zeros, ones에 값 추가됨
    if fiboN<len(zeros):
        print("%d %d"%(zeros[fiboN], ones[fiboN]))
        return
    for _ in range(fiboN-2):
        zeros.append(zeros[-2]+zeros[-1])
        ones.append(ones[-2]+ones[-1])
    print("%d %d"%(zeros[-1], ones[-1]))

def solutionFailed():
    #시간초과
    fiboN = int(input())
    queue = [fiboN]
    if queue[0]==0 or queue[0]==1:
        print("%d %d"%(queue.count(0), queue.count(1)))
        return
    
    while queue[0]!=1:
        divN = queue[0]
        popNum = queue.count(queue[0])
        queue = queue[popNum:] + [divN-1, divN-2]*popNum
        queue = sorted(queue)[::-1]
        # print('queue: ',queue)
    print("%d %d"%(queue.count(0), queue.count(1)))

if __name__=="__main__":
    testcase = int(input())
    for test in range(testcase):
        solution()