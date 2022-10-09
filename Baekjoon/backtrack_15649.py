
def solution(N, M):
    numRange = list(range(1, N+1))

    def makeChild(childList, M):
        returnVal = []
        if M==1: return [[child] for child in childList]
        for child in childList:
            temp=[child]
            tempList = childList.copy()
            tempList.remove(child)
            tempResult = [temp+child for child in makeChild(tempList, M-1)]
            # print('child is ',child,', result is ',tempResult)
            returnVal += tempResult

        return returnVal

    result = makeChild(numRange, M)
    for res in result:
        print(' '.join([str(el) for el in res]))

    return 0

inStream = input().split()
[N, M ]= [int(i) for i in inStream]
solution(N,M)