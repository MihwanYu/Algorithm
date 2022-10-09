
def solution(N, M):
    arr = list(range(1,N+1))

    def makeSeq(childarr, M):
        if M==1: return [[child] for child in childarr]
        returnArr=[]
        for num in childarr:
            childarrCopy = childarr[childarr.index(num)+1:]
            returnArr += [[num]+childarr for childarr in makeSeq(childarrCopy,M-1)]
        return returnArr

    resArr = makeSeq(arr, M)
    for arr in resArr:
        
        print(' '.join([str(n) for n in arr]))
    
    # for num in arr:
    #     print('=======NUM: %d======='%num)
    #     tempChildArr = arr[arr.index(num)+1:]
    #     temparr = [[num]+childarr for childarr in makeSeq(tempChildArr,M-1)]
    #     for arr in temparr:
    #         print(arr)
    #     print()






inStream = input().split()
[N, M ]= [int(i) for i in inStream]
solution(N,M)