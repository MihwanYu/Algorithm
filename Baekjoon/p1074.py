
def solution():
    N, r, c = map(int, input().split())
    #격자판 크기: 2^N x 2^N
    order = 0
    count = zloop(N,r,c)
    print(count)

def zloop(N,r,c):
    order = 0
    if N==0: return 0
    if r<2**(N-1):
        if c<2**(N-1):
            order = 0
            innerorder = zloop(N-1,r,c)
        else:
            order = 4**(N-1)
            innerorder = zloop(N-1, r, c-2**(N-1))
    else:
        if c<2**(N-1):
            order = 4**(N-1)*2
            innerorder = zloop(N-1, r-2**(N-1), c)
        else:
            order = 4**(N-1)*3
            innerorder = zloop(N-1, r-2**(N-1), c-2**(N-1))
    # print('N: %d, r: %d, c: %d, order: %d'%(N,r,c,order))
    return order+innerorder

if __name__=="__main__":
    solution()
