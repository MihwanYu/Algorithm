import math
def solution():
    L, R = map(int, input().split())
    if L==R:
        print(str(L).count('8'))
        return
    #L,R 자릿수가 다르면 무조건 0
    if len(str(L)) != len(str(R)):
        print(0)
        return
    diff = len(str(R-L))
    common=''
    i = 0
    while str(L)[i] == str(R)[i]:
        common += str(L)[i]
        i+=1
    # common = str(L)[:-diff]
    # print('common: ',common)
    print(common.count('8'))

if __name__=="__main__":
    solution()
