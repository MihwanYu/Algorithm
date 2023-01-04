
import math

def solution():
    # 가장 큰 둘레 길이 - 가장 작은 둘레 길이
    # 평.사 못 만들면 -1
    # abs(xa)<=5000
    xa,ya,xb,yb,xc,yc = map(int,input().split())
    #일직선상에 있는 경우 -> 기울기로 확인
    if xa==xb==xc:
        print(-1.0)
        return
    if xa!=xb and xa!=xc:
        if (ya-yb)/(xa-xb) == (ya-yc)/(xa-xc):
            print(-1.0)
            return

    len1 = getLength(xa,ya,xb,yb)
    len2 = getLength(xa,ya,xc,yc)
    len3 = getLength(xb,yb,xc,yc)
    if min([len1,len2,len3])==len1:
        largeRec = (len2+len3)*2
    elif min([len1,len2,len3])==len2:
        largeRec = (len1+len3)*2
    else:
        largeRec = (len1+len2)*2

    if max([len1,len2,len3])==len1:
        smallRec = (len2+len3)*2
    elif max([len1,len2,len3])==len2:
        smallRec = (len1+len3)*2
    else:
        smallRec = (len1+len2)*2
    
    print(largeRec-smallRec)

def getLength(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    


if __name__=="__main__":
    solution()