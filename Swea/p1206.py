# SW 기본 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

'''
각 테스트케이스의 첫 번째 줄에는 건물의 개수 N이 주어진다. (4 ≤ N ≤ 1000)
그 다음 줄에는 N개의 건물의 높이가 주어진다. (0 ≤ 각 건물의 높이 ≤ 255)
맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다. (예시에서 빨간색 땅 부분)
'''
# case1: N = 14, heights=0 0 3 5 2 4 9 0 6 4 0 6 0 0

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    print('#%d '%test_case, end='')
    N = int(input())
    heights = [int(i) for i in input().split()]
    # print('heights: ',heights)
    views = 0
    # for building in heights:
        # print('O'*building+'-'*(N-building))
        #heights idx들에 대해서, heights[i]가 heights[i-1],heights[i-2], heights[i+1], heights[i+1] 4개 값보다 클 때의 개수를 구해야함
        #ex) idx가 3-> idx1, idx2, idx4, idx5와의 차이를 구하고, 그 중 min값: min(5-0, 5-3, 5-2, 5-4) -> min(5,2,3,1)-> 1이 idx3의 조망권 수
    for idx in range(2, len(heights)-2):
        view = min([heights[idx]-heights[idx-2], heights[idx]-heights[idx-1], heights[idx]-heights[idx+1], heights[idx]-heights[idx+2]])
        if view>0:
            views +=view
            # print('view for %d: %d'%(idx, view))

    print(views)