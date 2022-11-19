#평탄화-> 가장 높 - 가장 낮 --> 최대 1
# 옮기고 나서 최고 / 최저 차이 반환
#가로길이 100, 높이 1~199, 덤프 1~1000
#덤프 내에 평탄화 완료하면 더 덤프 하지 말고 0 or 1 반환

T = int(input())
for test_case in range(1, T+1):

    dump = int(input())#덤프 횟수
    heights = list(map(int, input().split()))#상자의 높이값: 총 100개

    count = 0
    def dumping(count):
        global dump, heights
        if count==dump: return
        bigIdx = heights.index(max(heights))
        smallIdx = heights.index(min(heights))
        if(heights[bigIdx]-heights[smallIdx])<=1:
            # print('flattending.... should be return recursion')
            return
        #dump 작동
        heights[bigIdx] -=1
        heights[smallIdx] +=1

        #횟수 증가시키기
        dumping(count+1)


    dumping(count)
    print('#%d %d'%(test_case, max(heights)-min(heights)))
    # print('#%d %d%'%(test_case, (max(heights)-min(heights))))