import math

def solution():
    #원과 점의 위치관계(?): 두 점 start, end 사이에 그은 선이 원의 경계와 최소로 만나는 횟수
    #각 점이 몇 개의 원 내부에 있는가(같은 행성계에 있는 경우 행성계 중복 제거 -중복수*2)
    # -> distance((cX,cY), (pX,pY)) < cR일 경우 내부에 있음
    startX,startY,endX,endY = map(int, input().split())
    gal_num = int(input())
    startlist = []
    endlist = []
    for i in range(gal_num):
        cX, cY, cR = map(int, input().split())
        if distance(cX,cY,startX,startY)<cR:
            startlist.append(i)
        if distance(cX,cY,endX,endY)<cR:
            endlist.append(i)
    # print('result: ',startlist, endlist)
    # print(len(startlist)+len(endlist))
    # print('result: ',len(set(startlist+endlist)))
    if len(set(startlist+endlist)) != len(startlist+endlist):
        sameGalaxy = len(startlist+endlist) - len(set(startlist+endlist))
        print('result: ',len(startlist)+len(endlist)-sameGalaxy*2)
    else:
        print('result: ',len(startlist)+len(endlist))

def distance(cX,cY,pX,pY):
    return math.sqrt(abs(cX-pX)**2 + abs(cY-pY)**2)

if __name__=="__main__":
    testcase = int(input())
    for test in range(testcase):
        solution()