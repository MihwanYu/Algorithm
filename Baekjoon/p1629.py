# ref: https://st-lab.tistory.com/237
#알고리즘 분류: 분할정복 / 지수법칙과 모듈러 성질 ★
def solution():
    A,B,C = map(int, input().split())

    ans = mod(A,B,C)
    print('ans: %d'%ans)

def mod(A, exp, divmod):
    if exp==1:
        return A%divmod
    
    temp = mod(A, exp//2, divmod) #A가 2^9면 temp는 2^4

    if exp%2==0:
        return ( (temp * temp) )%divmod
    else:
        return ( (temp*temp) * (A) ) %divmod

def solution2():
    #시간초과 탈탈털린,,,
    A,B,C = map(int, input().split())
    ans = 1
    mods = []

    for _ in range(B):
        ans *= A
        # print("%d %% %d = %d"%(ans,C,ans%C))
        mods.append(ans%C)
        if mods.count(ans%C)==2:
            break
    # print('\nmods: ',mods)
    del mods[-1]
    loop_start = mods.index(ans%C)
    loop_mods = mods[loop_start:]
    idx = (B-loop_start)%(len(loop_mods))
    answer = loop_mods[idx-1]
    # print('loop_start: %d, ids: %d'%(loop_start, idx))
    print('%d'%(answer))

if __name__=="__main__":
    solution()