import math

# 두 원의 중심점, 반지름이 주어졌을 때 둘이 만나는 경우의 수
# 두 원의 위치관계만 잘 파악하면 됐던 문제
def solution():
    # 조규현 x,y 백승환 x,y 조규현과 류재명 r1, 백승환과 류재명 r2 dlsvnt
    # 류재명이 있을 수 있는 좌표 경우의 수. 가능성이 무한대면 -1
    # -10000 <= x,y <= 10000
    jo_x, jo_y, r1, ba_x, ba_y, r2 = map(int, input().split())
    dis = math.sqrt(abs(jo_x-ba_x)**2 + abs(jo_y-ba_y)**2)
    # print('dis: ',dis,", r1: %d, r2: %d"%(r1,r2))
    if dis==0 and r1==r2:
        #두 원이 동일-> 가능성 무한대
        print(-1)
    elif r1+r2==dis:
        #외접
        print(1)
    elif r1+r2<dis:
        #아예 외부
        print(0)
    elif abs(r1-r2)<dis and dis<r1+r2:
        #두 점에서
        print(2)
    elif abs(r1-r2)==dis:
        #내접
        print(1)
    elif abs(r1-r2)>dis and r1 !=r2:
        #원 내부에 다른 원
        print(0)
    
    
if __name__=="__main__":
    testcase = int(input())
    for test in range(testcase):
        solution()