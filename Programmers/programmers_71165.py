


def bfs(garden, blooms, visited):

    day = 0
    Q = [blooms]
    while Q:
        dailyblooms = Q.pop(0)
        # print('day %d: dailyblooms '%day, dailyblooms)
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        nextday = []
        for flower in dailyblooms:
            if visited[flower[0]][flower[1]] == True:continue
            garden[flower[0]][flower[1]] = 1
            visited[flower[0]][flower[1]] = True #꽃 리스트 방문 체크
            for i in range(4):
                newX = flower[0]+dx[i]
                newY = flower[1]+dy[i]
                if newX>=0 and newX<len(garden) and newY>=0 and newY<len(garden) and garden[newX][newY]==0:
                    if (newX,newY) not in dailyblooms:
                        nextday.append( (newX,newY) )

        if nextday:
            Q.append(list(set(nextday)))
        day +=1
    return day-1

def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    n = len(garden)
    blooms = []
    visited = [[False]*n for _ in range(len(garden))]
    for row in range(len(garden)):
        for col in range(len(garden[row])):
            if garden[row][col]==1:
                blooms.append( [row, col] )
    # print('blooms: ',blooms)			
    answer = bfs(garden, blooms, visited)
    
    
    
    
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
garden1 = [[0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0]]
garden1 = [[1,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,1,0]]
# garden1 = [[0,0,0], [0,1,1], [0,0,0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")